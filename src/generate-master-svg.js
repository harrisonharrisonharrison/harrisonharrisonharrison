const fs = require('fs');

// 1. Load all assets, including the new Lightbulb
const grass = fs.readFileSync('./assets/grass.svg', 'utf8');
const identity = fs.readFileSync('./assets/identity.svg', 'utf8');
const projects = fs.readFileSync('./assets/projects.svg', 'utf8');
const statistics = fs.readFileSync('./assets/statistics.svg', 'utf8');
const contact = fs.readFileSync('./assets/contact.svg', 'utf8');
const lightbulb = fs.readFileSync('./assets/Lightbulb.svg', 'utf8');

const svgCSS = `
  <style>
    /* Zone Container */
    .asset-zone {
      cursor: crosshair;
    }

    /* Background Assets (Signs, Rocks) - Dimmed initially */
    .bg-asset {
      opacity: 0.2;
      transition: opacity 0.3s ease-in-out;
    }

    /* Body Text - Completely hidden initially */
    .body-text {
      opacity: 0;
      transition: opacity 0.4s ease-in-out;
    }

    /* Hover States - Triggered when hovering over individual zones */
    .asset-zone:hover .bg-asset {
      opacity: 1.0;
    }
    
    .asset-zone:hover .body-text {
      opacity: 1.0;
    }

    /* Lightbulb Reveal Trigger */
    .reveal-all {
      cursor: pointer;
      transition: filter 0.3s ease;
      opacity: 0.2;
    }
    
    /* Optional: Make the lightbulb itself glow when hovered */
    .reveal-all:hover {
      filter: drop-shadow(0px 0px 8px rgba(255, 255, 255, 0.8));
      opacity:1.0;
    }

    /* Reveal All Logic - Targets all following .asset-zone siblings */
    .reveal-all:hover ~ .asset-zone .bg-asset,
    .reveal-all:hover ~ .asset-zone .body-text {
      opacity: 1.0;
    }
  </style>
`;

const masterSVG = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="800" height="500">
  ${svgCSS}
  
  <rect width="100%" height="100%" fill="#2b2b2b" />

  <g transform="translate(0, 359)">
    ${grass}
  </g>

  <g class="reveal-all" transform="translate(353, 0)">
    ${lightbulb}
  </g>

  <g class="asset-zone" transform="translate(0, 0)">
    <g class="bg-asset">
      ${identity}
    </g>
    <g class="body-text">
      <text x="80" y="160" fill="#ffffff" font-family="monospace" font-size="16">Hi, I'm Harrison Tran</text>
      <text x="100" y="180" fill="#aaaaaa" font-family="monospace" font-size="14">> Full-Stack Developer</text>
    </g>
  </g>

  <g class="asset-zone" transform="translate(389, 0)">
    <g class="bg-asset">
      ${projects}
    </g>
    <g class="body-text">
      <text x="10" y="85" fill="#ffffff" font-family="monospace" font-size="16">Featured Projects:</text>
    </g>
  </g>

  <g class="asset-zone" transform="translate(520, 199)">
    <g class="bg-asset">
      ${statistics}
    </g>
    <g class="body-text">
      <text x="30" y="70" fill="#ffffff" font-family="monospace" font-size="16">GitHub Ledger</text>
    </g>
  </g>

  <g class="asset-zone" transform="translate(113, 350)">
    <g class="bg-asset">
      ${contact}
    </g>
    <g class="body-text">
      <text x="100" y="70" fill="#ffffff" font-family="monospace" font-size="16">Ping Me</text>
      <text x="100" y="95" fill="#aaaaaa" font-family="monospace" font-size="14">linkedin.com/in/htran</text>
    </g>
  </g>

</svg>
`;

fs.writeFileSync('fog-of-war.svg', masterSVG);
console.log('Master SVG successfully generated');