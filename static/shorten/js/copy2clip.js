$(document).ready(function myFunction() {
  $("#copyBtna").click(function () {
    var copyText = document.getElementById("shortUrla");
    console.log("A")
    copyText.select();
    copyText.setSelectionRange(0, 99999)
    document.execCommand("copy");
  })
  $("#copyBtnb").click(function () {
    var copyText = document.getElementById("shortUrlb");
    console.log("B")
    copyText.select();
    copyText.setSelectionRange(0, 99999)
    document.execCommand("copy");
  })
})
