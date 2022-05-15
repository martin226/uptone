<template>
  <div class="flex flex-col items-center w-full">
    <div class="w-8/12 space-y-8">
      <h1 class="uppercase text-4xl font-bold text-center text-primary">
        Our Mission
      </h1>
      <div
        class="grid grid-cols-1 space-x-16 justify-center items-center"
        md="grid-cols-2"
      >
        <div class="space-y-4">
          <p class="leading-loose text-xl">
            ToneUp is an AI-powered web extension that scans your Twitter feed
            for hate speech and negativity, alerting you of toxic tweets and
            allowing you to mute them. By filtering out the noise, Uptone allows
            you to focus on what matters to you.
          </p>
        </div>
        <img src="@/assets/img/undraw_love_re_mwbq.svg" alt="Spread Love" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'LandingMission',
});
</script>
