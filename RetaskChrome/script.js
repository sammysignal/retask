window.onload = function () {
  var jq = document.createElement('script');
  jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js";
  document.getElementsByTagName('body')[0].appendChild(jq);
  var gmsrc = document.createElement('script');
  gmsrc.src = "https://xmailchrome.appspot.com/gmail.js";
  document.getElementsByTagName('body')[0].appendChild(gmsrc);
  console.log("Scripts loaded, Start playing ...");
  console.log("Sameer was heer FROM RETASK!");
}