import "webext-base-css";
import "./options.css";

import optionsStorage from "./options-storage.js";

async function init() {
  await optionsStorage.syncForm("#options-form");
}

init();
