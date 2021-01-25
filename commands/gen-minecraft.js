const Discord = require('discord.js');
const fs = require('fs');
const cooldown = new Set();

module.exports.run = async (client, msg, args, config) => {
    if(cooldown.has(msg.author.id)) {
        msg.reply(`You need to wait ${config.COOLDOWN} minutes to use this command again!`)
            .then((m) => {
                msg.delete();

                setTimeout(() => {
                    m.delete();
                }, 5000);
            });
    } else {
        fs.readFile('./accounts/minecraft.txt', 'utf8', function(err, data) {
            if (err) throw err;

            data = data + '';
            var lines = data.split('\n');
            let account = lines[Math.floor(Math.random() * 1)];

            fs.writeFile('./accounts/minecraft.txt', lines.slice(1).join('\n'), function(err) {
                if(err) throw err;
            });

            let embed = new Discord.MessageEmbed()
            .addField('LinkGen', `https://discord.gg/JqDAbN8Stq`)
            .addField('Minecraft Account',`\n**${account}**`)
            .setColor("#363940")
            .setFooter('Bot made by Snikker#1337')
            .setTimestamp();

            msg.author.send(embed);

var xd = new Discord.MessageEmbed()
        .setColor("#ff0000")
        .setTitle("CHECK YOUR DM")
      
        .setThumbnail("https://cdn.discordapp.com/attachments/773133136929226763/797204521997828106/777514274829893683.gif")
        .setFooter("LinkGen")
        .setTimestamp()
        .setDescription("I've sent you 1 Minecraft Account!")

                
msg.reply(xd).then(m => {
                    setTimeout(() => {
                    }, 900000);
                });

	
            cooldown.add(msg.author.id);
            setTimeout(() => {
                cooldown.delete(msg.author.id);
            }, config.COOLDOWN * 60 * 1000);
		});
    }
};

module.exports.help = {
    name: `gen minecraft`,
    description: `Sends you a Minecraft Account!`
};