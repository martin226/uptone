<template>
  <div class="flex flex-col items-center w-full">
    <div class="w-8/12 space-y-8">
      <h1 class="uppercase text-4xl font-bold text-center text-primary">
        About Us
      </h1>
      <div
        class="grid grid-cols-1 justify-center items-center"
        md="grid-cols-3 space-x-16"
      >
        <div
          class="grid grid-cols-1 gap-8 justify-center items-center"
          md="grid-cols-2 grid-rows-2"
        >
          <img
            src="@/assets/img/martin.png"
            alt="Martin"
            class="border-4 border-primary m-auto"
          />
          <img
            src="@/assets/img/emily.png"
            alt="Emily"
            class="border-4 border-primary m-auto"
          />
          <img
            src="@/assets/img/nicholas.png"
            alt="Nicholas"
            class="border-4 border-primary m-auto"
          />
          <img
            src="@/assets/img/ahtesham.png"
            alt="Ahtesham"
            class="border-4 border-primary m-auto"
          />
        </div>
        <p class="leading-loose text-xl mt-4" md="col-span-2 mt-0">
          Having gone through many world changing events such as COVID-19, many
          may feel overwhelmed by the amount of negativity the world has to
          offer. With the rise of negative media and the constant toxic noise
          that surrounds us everyday, Uptone aims to push that all out and allow
          users to focus on what matters most. In light of the recent buyout of
          Twitter and the upcoming policy change that would see the freedom of
          all speech being permitted on Twitter, Uptone was born. Using
          sentiment analysis and a convolutional neural network, the team at
          Uptone has developed a web extension that aims to limit the constant
          negative noise that takes over our Twitter feeds.
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'LandingAbout',
});
</script>
