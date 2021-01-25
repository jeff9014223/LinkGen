const Discord = require ("discord.js")

exports.run = async (client, message) => {
  let embed = new Discord.MessageEmbed()
	.setColor('#0099ff')
	.setTitle('LinkGen Help')
	.setURL('https://discord.gg/sQXKeJKEza')
	.setAuthor('Snikker#1337', 'https://i.imgur.com/HiFP9va.gif', 'https://discord.gg/sQXKeJKEza')
	.setDescription('Commands: \n ?gen-nitro \n ?gen-nordvpn \n ?gen-spotify \n ?gen-netflix \n ?gen-creditcard \n ?gen-hulu \n ?gen-disney \n ?gen-pornhub \n ?gen-minecraft \n ?gen-pandora ')
	.setThumbnail('https://imgur.com/Y6pbfXG.png')
	.setTimestamp()
	.setFooter('LinkGen @2021');

message.channel.send(embed);
}
module.exports.help = {
  name: 'help'
}
