const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client();

client.on('qr', (qr) => {
    // Generate and scan this QR code using your WhatsApp mobile app
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Bot is ready!');
});

client.on('message', message => {
    if (message.body === '!help') {
        message.reply('Here is a list of commands: !youtube [link]');
    }
});

client.initialize();
