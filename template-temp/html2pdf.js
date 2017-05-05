var page = new WebPage();
var system = require("system");
page.paperSize = {
  format: "A4",
  orientation: "portrait",
  margin: {
    left: "0cm",
    right: "0cm",
    top: "0cm",
    bottom: "0cm"
  }
};

page.zoomFactor = 1.0;
page.open(system.args[1], {
    encoding: "utf8"
  },
  function (status) {
  setTimeout(function() {
    page.render(system.args[2]);
    phantom.exit();
  }, 0);
});
