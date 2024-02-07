$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
});
