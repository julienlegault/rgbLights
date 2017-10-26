var redRGB;
var greenRGB;
var blueRGB;
var hexCode;
var colorPick;
var sunTime;
var userCode;

function onload() {
   redRGB = document.getElementById("redRGB");
   greenRGB = document.getElementById("greenRGB");
   blueRGB = document.getElementById("blueRGB");
   hexCode = document.getElementById("hexCode");
   colorPick = document.getElementById("colorPick");
   sunTime = document.getElementById("sunTime");
   userCode = document.getElementById("userCode");
}

function setBackground(color) {
   document.body.style.backgroundColor = color;
}

function sendrgb() {
   var combinedString = "rgb(";
   combinedString += redRGB.value + ",";
   combinedString += greenRGB.value + ",";
   combinedString += blueRGB.value + ")";
   setBackground(combinedString);
}

function sendhex() {
   var combinedString = "hex(";
   combinedString += hexCode.value + ")";
   setBackground("#" + hexCode.value);
}

function sendcolorpick() {
   setBackground(colorPick.value);
}

function warEagle() {
   setBackground("#dd550c");
}

function sunrise() {
   setBackground("rgb(255,128,64)");
}

function sendusercode() {
   alert(userCode.value);
}
