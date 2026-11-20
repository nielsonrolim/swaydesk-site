// The demo video's chapters: a click seeks the player on the page instead of opening the file.
(function () {
  var video = document.getElementById("demo-video");
  if (!video) return;
  document.querySelectorAll(".demo__chapters a[data-t]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      var t = Number(a.dataset.t);
      if (!isFinite(t)) return;
      e.preventDefault();
      var seek = function () {
        video.currentTime = t;
        var p = video.play();
        if (p && p.catch) p.catch(function () {});
      };
      if (video.readyState >= 1) seek();
      else { video.addEventListener("loadedmetadata", seek, { once: true }); video.load(); }
      video.scrollIntoView({ block: "nearest", behavior: "smooth" });
      video.focus({ preventScroll: true });
    });
  });
})();
