$(document).ready(function () {
  $('.email-bar').click(function () {
      var emailData = this.getElementsByClassName('email-data')[0].innerHTML;
      console.log(emailData);
      var bodyChunks = emailData.split("'");
      console.log("bC = " + JSON.stringify(bodyChunks));
      var chunkString = "";
      for (var i = 0; i < bodyChunks.length; i++) {
        if (!bodyChunks[i] == ", " && !bodyChunks[i] == "[" && !bodyChunks[i] == "]") {
          chunkString = chunkString + bodyChunks[i];
        }
      }
      document.write(chunkString);
  });
});