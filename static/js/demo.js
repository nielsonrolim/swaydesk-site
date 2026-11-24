// The demo video. On the home page, the player starts dimmed behind a play button (without JS it's a plain
// player with controls); the first play brings the controls back. The chapters seek the player on the page
// instead of opening the file.
(function () {
  var video = document.getElementById("demo-video");
  if (!video) return;
  var frame = video.closest(".video.is-idle");
  var play = frame && frame.querySelector("[data-video-play]");
  if (play) {
    var wake = function () {
      frame.classList.remove("is-idle");
      play.hidden = true;
      video.controls = true;
    };
    video.controls = false;
    play.hidden = false;
    play.addEventListener("click", function () {
      wake();
      var p = video.play();
      if (p && p.catch) p.catch(function () {});
      video.focus({ preventScroll: true });
    });
    video.addEventListener("play", wake);
  }
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
