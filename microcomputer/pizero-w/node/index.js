const awsIot = require('aws-iot-device-sdk')

const interval = 5;

/**
 * Sensor type to read from.
 *
 * Possible values are:
 *
 * DHT11:  11
 * DHT22:  22
 * AM2302: 22
 */
const sensorType = 22;


// sensor gpio pin number
const sensorPin = 4;

const sensorLib = require('node-dht-sensor');

const sensor = {
  initialize: function () {
    return sensorLib.initialize(
      parseInt(sensorType, 10),
      parseInt(sensorPin, 10)
    );
  },
  read: function () {
    const data = sensorLib.read();
    const temperature = data.temperature.toFixed(2);
    const humidity = data.humidity.toFixed(2);

    if (temperature !== 0 || humidity !== 0) {
      console.log(
        '\tTemperature: ' + temperature + ' °C',
        '\tHumidity: ' + humidity + '%');
     // TODO : publish to AWS IoT
    }
    setTimeout(sensor.read, interval * 1000);
  }
};

if (sensor.initialize()) {
  console.log('Initialized sensor...');
  // TODO replace variables with your values
  const device = awsIot.device({
    keyPath: 'PRIVATE_KEY.key',
    certPath: 'CERTIFICATE.pem',
    caPath: 'ROOT_CERTIFICATE.pem',
    clientId: 'YOUR_THING_NAME',
    host: 'TOT_ENDPOINT_FOR_YOUR_AWS_ACCOUNT'
  });
 
  device.on('connect', () => {
    console.log('Connected to AWS IoT');
    sensor.read();
  });
  
  device.on('disconnect', (reason) => {
    console.error(`Disconnected from AWS IoT: ${reason}`);
  });

  device.on('error', (err) => {
    console.error('Error interacting with AWS IoT');
    console.error(err); 
  });
} else {
  console.error('Failed to initialize sensor');
}
