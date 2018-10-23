/************************************************************************************
Event Listeners
************************************************************************************
function createEventListeners(){
  calcTimeZone()
}

function calcTimeZone(){
  var d = new Date();
  var n = d.getTimezoneOffset();
  console.log(n);
}


************************************************************************************
Function Calls
************************************************************************************

if (window.addEventListener){
  window.addEventListener("load", createEventListeners, false);
} else if(window.attachEvent){
  window.attachEvent("onload", createEventListeners);
}
*/
