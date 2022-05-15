import OptionsSync from "webext-options-sync";

export default new OptionsSync({
  defaults: {
    offensiveLanguage: false,
    hateSpeech: true,
  },
  migrations: [OptionsSync.migrations.removeUnused],
  logging: true,
});
