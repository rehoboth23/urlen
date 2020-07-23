$(document).ready(function myFunction() {
  $("#gitRepo").click(() => {
    var copyText = document.getElementById("gitHolder");
    copyText.select();
    copyText.setSelectionRange(0, 99999)
    document.execCommand("copy");
  })
})