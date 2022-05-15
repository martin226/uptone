<template>
  <div class="bg-secondary">
    <Hero class="min-h-screen flex-1 border-b-1 border-black" />
    <Mission class="py-16" />
    <How class="py-16" />
    <About class="py-16" />
    <Footer class="py-8" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'IndexPage',
});
</script>
