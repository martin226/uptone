<template>
  <div class="flex flex-col items-center w-full">
    <div class="w-8/12 space-y-8">
      <h1 class="uppercase text-4xl font-bold text-center text-primary">
        How It Works
      </h1>
      <div
        class="grid grid-cols-1 space-x-16 justify-center items-center"
        lg="grid-cols-2"
      >
        <div
          class="flex justify-center items-center border-4 border-primary order-last mt-4"
          lg="order-first mt-0"
        >
          <img src="@/assets/img/step_1.png" alt="Step 1" />
        </div>
        <div class="space-y-4">
          <div
            class="text-center bg-primary text-white rounded-full w-24 h-24 flex justify-center items-center text-4xl ml-auto"
          >
            1
          </div>
          <p class="leading-loose text-lg" md="text-xl">
            Download our extension and install it on your browser. Our extension
            is compatible with all major browsers!
          </p>
        </div>
      </div>
      <div
        class="grid grid-cols-1 space-x-16 justify-center items-center"
        lg="grid-cols-2"
      >
        <div
          class="flex justify-center items-center border-4 border-primary mt-4 order-last"
          lg="mt-0"
        >
          <img src="@/assets/img/step_2.png" alt="Step 2" />
        </div>
        <div class="space-y-4">
          <div
            class="text-center bg-primary text-white rounded-full w-24 h-24 flex justify-center items-center text-4xl mr-auto"
          >
            2
          </div>
          <p class="leading-loose text-lg" md="text-xl">
            Adjust any of the settings in the extension to your liking. You can
            choose to hide hate speech, offensive language, or both.
          </p>
        </div>
      </div>
      <div
        class="grid grid-cols-1 space-x-16 justify-center items-center"
        lg="grid-cols-2"
      >
        <div
          class="flex justify-center items-center border-4 border-primary order-last mt-4"
          lg="order-first mt-0"
        >
          <img src="@/assets/img/step_3.png" alt="Step 3" />
        </div>
        <div class="space-y-4">
          <div
            class="text-center bg-primary text-white rounded-full w-24 h-24 flex justify-center items-center text-4xl ml-auto"
          >
            3
          </div>
          <p class="leading-loose text-lg" md="text-xl">
            Let our neural network do its magic! You can now hide toxic tweets
            from your timeline and keep your feed clean. If you want to unhide a
            tweet for any reason, you can do so by clicking on the "View"
            button.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'LandingHow',
});
</script>
