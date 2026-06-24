var feedback = document.forms.feedback;
feedback.hidden = false;

feedback.addEventListener("submit", function (ev) {
  ev.preventDefault();

  var page = document.location.pathname;
  var data = ev.submitter.getAttribute("data-md-value");

  console.info(`Feedback provided on: ${page}, value: ${data}`);

  if (window._paq) {
    window._paq.push([
      'trackEvent',
      'Feedback', // The category of the event
      page, // The page-URL the feedback was provided on
      data.toString() === '1' ? 'Y' : 'N', // The feedback value (in human-readable form)
      data, // The quantifiable value (to accumulate all the feedback values)
    ]);
  }

  // Disable/hide the UI
  feedback.firstElementChild.disabled = true;

  var inputs = feedback.querySelector(".md-feedback__list");
  if (inputs) inputs.hidden = true;

  var note = feedback.querySelector(
    ".md-feedback__note [data-md-value='" + data + "']"
  );
  if (note) note.hidden = false;
});
