$(document).ready(function() {

  $("body").attr({
    "data-spy": "scroll",
    "data-target": ".bs-docs-sidebar"
  })

  for (var i = 1; i < 6; i++) {
    var select = "h" + i;
    $(select).removeAttr("id")
  }

  var toc = "";
  var level = 1;

  function replacer(str, openLevel, titleText, closeLevel) {
    if (openLevel != closeLevel) {
      return str;
    }

    if (openLevel > level) {
      toc += (new Array(openLevel - level + 1)).join("<ul class=\"nav\">");
    } else if (openLevel < level) {
      toc += "</li>"
      toc += (new Array(level - openLevel + 1)).join("</ul>");
    }
    else if (level != 1)
    {
      toc += "</li>"
    }

    level = parseInt(openLevel);

    var anchor = titleText.replace(/ /g, "_");
    
    toc += "<li><a href=\"#" + anchor + "\">" + titleText
      + "</a>";

    return "<h" + openLevel + " id=" + anchor + ">" + titleText + "</h" + closeLevel + ">";
  }

  document.getElementById("post-body").innerHTML = 
    document.getElementById("post-body").innerHTML.replace(/<h([\d])>([^<]+)<\/h([\d])>/gi, replacer);

  if (level) {
    toc += (new Array(level + 1)).join("</li></ul>");
  }

  document.getElementById("toc").innerHTML += toc;

  $("aside nav ul").first().addClass("bs-docs-sidenav");

  $("#toc").affix({
    offset: {
      top: $('#toc').offset().top,
      bottom: $('footer').outerHeight(true)
    }
  });
})
