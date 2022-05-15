// eslint-disable-next-line import/no-unassigned-import
import "webext-base-css";
import "./options.css";

// Don't forget to import this wherever you use it
import browser from "webextension-polyfill";

import optionsStorage from "./options-storage.js";

async function init() {
  await optionsStorage.syncForm("#options-form");
}

init();
