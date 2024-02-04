const awsIot = require('aws-iot-device-sdk')

const interval = 3;

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
let device;

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
    console.log('Entering sensor.read...');
    const data = sensorLib.read();
    const temperature = data.temperature.toFixed(2);
    const humidity = data.humidity.toFixed(2);

    if (temperature !== 0 || humidity !== 0) {
      console.log(
        '\tTemperature: ' + temperature + ' °C',
        '\tHumidity: ' + humidity + '%');
      device.publish('YOUR_TOPIC', JSON.stringify({ temperature, humidity }));
    }
    setTimeout(sensor.read, interval * 1000);
  }
};

if (sensor.initialize()) {
  console.log('Initialized sensor...');
  // TODO replace variables with your values
  device = awsIot.device({
    keyPath: './YOUR_KEY.private.key',
    certPath: './YOUR_CERTIFICATE.cert.pem',
    caPath: './AmazonRootCA1.pem',
    clientId: 'YOUR_THING_NAME',
    host: 'a1ykoqoe4qq7d0-ats.iot.us-west-2.amazonaws.com',
    debug: true
  });
  console.log('MQTT wrapper created!');
  console.log(device);
 
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
