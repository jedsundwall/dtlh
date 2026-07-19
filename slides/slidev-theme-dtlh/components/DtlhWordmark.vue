<!-- The stacked "Downtown / Loyal Heights" wordmark from the dtlh.org masthead.
     Sizing via font-size utilities on the component (e.g. class="text-5xl");
     color defaults to brand pink, override with text-[...] if ever needed. -->
<template>
  <div class="dtlh-wordmark" aria-label="Downtown Loyal Heights">
    <span>Downtown</span><br>
    <span>Loyal Heights</span>
  </div>
</template>

<style scoped>
.dtlh-wordmark {
  font-family: 'Germania One', serif;
  color: var(--dtlh-pink, #B53050);
  line-height: 0.92;
  letter-spacing: 0.005em;
  display: inline-block;
}
</style>
