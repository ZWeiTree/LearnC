let bgMusic = [];

bgMusic[0] = "Empty\ Throne";
bgMusic[1] = "Phoenix";
bgMusic[2] = "Utopia";
bgMusic[3] = "赤城";
bgMusic[4] = "闭目寻光";

let randomBgIndex = Math.round( Math.random() * 4 );

document.write('<source src="Music/'+bgMusic[randomBgIndex]+'.mp3" type="audio/mp3"></source>');
document.write('<source src="Music/'+bgMusic[randomBgIndex]+'.ogg" type="audio/ogg"></source>');
document.write('<embed height="50px" width="100px" src="Music/'+bgMusic[randomBgIndex]+'.mp3"></embed>');
