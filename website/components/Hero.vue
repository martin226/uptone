<template>
  <div class="px-12 py-36 flex flex-col" md="px-48">
    <img src="@/assets/img/logo.svg" alt="Logo" class="w-16 h-16" />
    <div class="flex flex-col justify-center h-full flex-1">
      <h1
        class="uppercase font-bold text-5xl w-9/12 text-primary"
        md="text-6xl"
        xl="text-[5rem]"
      >
        Keep the web on an uplifting tone, with Uptone.
      </h1>
    </div>
    <a
      href="https://github.com/martin226/uptone"
      class="mx-auto uppercase py-3 px-16 font-semibold border-4 border-primary text-primary text-center"
      md="text-xl"
      xl="text-2xl py-4 px-32"
    >
      Download Now
    </a>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'LandingHero',
});
</script>
