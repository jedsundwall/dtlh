<script setup>
import { useNav } from '@slidev/client'
import { computed } from 'vue'
const { currentSlideRoute } = useNav()
const hide = computed(() => currentSlideRoute?.value?.meta?.slide?.frontmatter?.hideLogomark)
</script>

<!-- Faint DTLH mark, bottom-right, like the Radiant logomark footer.
     Suppress per-slide with `hideLogomark: true` in that slide's frontmatter. -->
<template>
  <footer v-if="!hide" class="fixed bottom-4 right-6 z-10 pointer-events-none dtlh-footer-mark">
    DTLH
  </footer>
</template>

<style scoped>
.dtlh-footer-mark {
  font-family: 'Germania One', serif;
  font-size: 1.05rem;
  letter-spacing: 0.04em;
  color: #B53050;
  opacity: 0.45;
}
</style>
