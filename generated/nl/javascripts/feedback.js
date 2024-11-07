var feedback = document.forms.feedback;
feedback.hidden = false;

feedback.addEventListener("submit", function (ev) {
  ev.preventDefault();

  var page = document.location.pathname;
  var data = ev.submitter.getAttribute("data-md-value");

  console.info(`Feedback provided on: ${page}, value: ${data}`);

  // Send feedback to AppInsights, if available
  if (appInsights) {
    appInsights.trackEvent({
      name: "feedback",
      properties: {
        page: page,
        value: data,
      },
    });
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
