/**
 * One-shot: create bare Research Brief submit Form bound to this spreadsheet.
 * Open the Submit Log sheet → Extensions → Apps Script → paste → run createResearchBriefSubmitForm.
 *
 * Spreadsheet ID expected: Research Brief — Submit Log
 * Does not require MCP Forms API.
 */
function createResearchBriefSubmitForm() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var form = FormApp.create('Research Brief — Submit');
  form.setDescription(
    'Bare functional submit for research briefs. Working draft stays a Google Doc; this form is the process packet. Schema v0.1.'
  );
  form.setCollectEmail(true);

  form.addTextItem().setTitle('gdoc_url').setHelpText('Working Google Doc URL').setRequired(true);
  form.addTextItem().setTitle('title').setRequired(true);
  form.addTextItem().setTitle('author').setHelpText('First Last').setRequired(true);

  form.addListItem().setTitle('org_unit').setChoiceValues(['Haptic', 'NascenTech', 'Other']).setRequired(true);
  form.addTextItem().setTitle('team_code').setHelpText('BS MC BA TD EX XX — optional');
  form.addParagraphTextItem().setTitle('core_question_own_words').setRequired(true);
  form.addTextItem().setTitle('origination').setHelpText('Who/how triggered — optional');

  form
    .addListItem()
    .setTitle('version_intent')
    .setChoiceValues(['first_review_v1', 'minor_bump', 'still_draft', 'major_rescope'])
    .setRequired(true);

  form
    .addListItem()
    .setTitle('submit_route')
    .setChoiceValues(['form', 'skill_cli', 'drive_handoff', 'email', 'dropper_later'])
    .setRequired(true);

  form.addParagraphTextItem().setTitle('for_levi').setHelpText('Recommendation · decision · next move');
  form.addParagraphTextItem().setTitle('author_reflection');

  form
    .addListItem()
    .setTitle('provenance_mode')
    .setChoiceValues(['mostly_me', 'mixed', 'mostly_ai', '(skip)']);

  form.addTextItem().setTitle('provenance_tools').setHelpText('Claude / Grok / none / other');

  form.addCheckboxItem().setTitle('checklist_read_fully').setChoiceValues(['I read the full brief after the last generative pass']).setRequired(true);
  form.addCheckboxItem().setTitle('checklist_cues_removed').setChoiceValues(['Cue lines removed']);
  form.addParagraphTextItem().setTitle('notes');

  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  // Store URL on _meta if present
  var meta = ss.getSheetByName('_meta');
  if (meta) {
    meta.appendRow(['form_url', form.getEditUrl()]);
    meta.appendRow(['form_published_url', form.getPublishedUrl()]);
    meta.appendRow(['form_created_at', new Date().toISOString()]);
  }

  Logger.log('Form edit: ' + form.getEditUrl());
  Logger.log('Form public: ' + form.getPublishedUrl());
  return form.getPublishedUrl();
}
