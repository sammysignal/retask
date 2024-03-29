// window.onload = function () {

// }

(function(funcName, baseObj) {
// The public function name defaults to window.docReady
// but you can pass in your own object and own function name and those will be used
// if you want to put them in a different namespace
funcName = funcName || "docReady";
baseObj = baseObj || window;
var readyList = [];
var readyFired = false;
var readyEventHandlersInstalled = false;

// call this when the document is ready
// this function protects itself against being called more than once
function ready() {
  if (!readyFired) {
  // this must be set to true before we start calling callbacks
  readyFired = true;
  for (var i = 0; i < readyList.length; i++) {
      // if a callback here happens to add new ready handlers,
      // the docReady() function will see that it already fired
      // and will schedule the callback to run right after
      // this event loop finishes so all handlers will still execute
      // in order and no new ones will be added to the readyList
      // while we are processing the list
      readyList[i].fn.call(window, readyList[i].ctx);
    }
  // allow any closures held by these functions to free
  readyList = [];
}
}

function readyStateChange() {
  if ( document.readyState === "complete" ) {
    ready();
  }
}

// This is the one public interface
// docReady(fn, context);
// the context argument is optional - if present, it will be passed
// as an argument to the callback
baseObj[funcName] = function(callback, context) {
// if ready has already fired, then just schedule the callback
// to fire asynchronously, but right away
if (readyFired) {
  setTimeout(function() {callback(context);}, 1);
  return;
} else {
  // add the function and context to the list
  readyList.push({fn: callback, ctx: context});
}
// if document already ready to go, schedule the ready function to run
if (document.readyState === "complete") {
  setTimeout(ready, 1);
} else if (!readyEventHandlersInstalled) {
  // otherwise if we don't have event handlers installed, install them
  if (document.addEventListener) {
      // first choice is DOMContentLoaded event
      document.addEventListener("DOMContentLoaded", ready, false);
      // backup is window load event
      window.addEventListener("load", ready, false);
    } else {
      // must be IE
      document.attachEvent("onreadystatechange", readyStateChange);
      window.attachEvent("onload", ready);
    }
    readyEventHandlersInstalled = true;
  }
}
})("docReady", window);


docReady(function() {
	function check(){

    // var gmail;


    // function refresh(f) {
    //   if( (/in/.test(document.readyState)) || (undefined === Gmail) ) {
    //     setTimeout('refresh(' + f + ')', 10);
    //   } else {
    //     f();
    //   }
    // }


    // var main = function(){
    //   // NOTE: Always use the latest version of gmail.js from
    //   // https://github.com/KartikTalwar/gmail.js
    //   gmail = new Gmail();
    //   console.log('Hello,', gmail.get.user_email());
    // }
    // refresh(main);

      var jq = document.createElement('script');
  jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js";
  document.getElementsByTagName('body')[0].appendChild(jq);
  var gmsrc = document.createElement('script');
  gmsrc.src = "https://xmailchrome.appspot.com/gmail.js";
  document.getElementsByTagName('body')[0].appendChild(gmsrc);
  g = new Gmail();
  console.log("Scripts loaded, Start playing ...");
  console.log("Sameer was heer FROM RETASK!");
  console.log("Hello " + g.get.user_email() + "!");

    // //console.log("hello from Retask! You must be " + document.getElementsByClassName('gb_P gb_R')[0].innerHTML + "!");
    // //console.log(document.getElementById(':2o'));
    // //console.log($('.aeH'))
    // var c, r, t;
    // t = document.createElement('table');
    // r = t.insertRow(0); 
    // c = r.insertCell(0);
    // c.innerHTML = 123;
    // c = r.insertCell(1);
    // c.innerHTML = 456;
    // t.className = "TestTable";
    // $('.aeH').appendChild(t);

    // // make Retask Button
    // console.log($('aic'))
    // retaskButton = document.createElement('div');
    // retaskButton.className = "retaskButton";
    // retaskButton.style.width = "155px";
    // retaskButton.style.height = "37px";
    // retaskButton.style.background = "red";
    // retaskButton.innerHTML = "Compose task";
    // $('.aic').appendChild(retaskButton);
  }
  check();
});