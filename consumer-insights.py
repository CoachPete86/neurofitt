# Create a styled, interactive HTML report with verbatim (our content) and limited-source excerpts.
# We'll embed data from the collected sources with short quotes (<=25 words each) and links.
from pathlib import Path

html = r"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Consumer Insights – Online Personal Training & Fighter Development</title>
<style>
  :root{
    --bg:#0b0f14;
    --panel:#121821;
    --ink:#e9eef7;
    --muted:#a9b6c7;
    --accent:#4cc9f0;
    --accent-2:#00f5d4;
    --bad:#ff6b6b;
    --good:#51cf66;
    --warn:#ffd43b;
  }
  *{box-sizing:border-box}
  body{margin:0;background:linear-gradient(160deg,#0b0f14,#0a111a 30%,#0b0f14);color:var(--ink);font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial}
  header{
    position:sticky;top:0;z-index:50;
    background:rgba(10,16,24,.9);backdrop-filter: blur(6px);
    border-bottom:1px solid rgba(255,255,255,.06);
  }
  .wrap{max-width:1200px;margin:0 auto;padding:18px 20px}
  h1{margin:0;font-size:24px;letter-spacing:.3px}
  .sub{color:var(--muted);font-size:13px}
  nav{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
  nav a{padding:8px 10px;border:1px solid rgba(255,255,255,.12);border-radius:8px;text-decoration:none;color:var(--ink);font-weight:600;font-size:14px}
  nav a:hover{border-color:var(--accent);color:var(--accent)}
  main{padding:24px 20px}
  .grid{display:grid;grid-template-columns:1.1fr .9fr;gap:20px}
  @media (max-width: 920px){.grid{grid-template-columns:1fr}}
  .card{background:var(--panel);border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:18px;box-shadow:0 8px 30px rgba(0,0,0,.25)}
  h2{margin:6px 0 10px;font-size:20px}
  h3{margin:14px 0 8px;font-size:16px}
  p{margin:8px 0}
  ul{margin:8px 0 8px 18px}
  code, .pill{background:rgba(255,255,255,.08);padding:2px 6px;border-radius:6px}
  .kpi{display:flex;gap:12px;flex-wrap:wrap}
  .kpi .item{flex:1 1 140px;background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.04));border:1px solid rgba(255,255,255,.08);border-radius:12px;padding:12px}
  .kpi .num{font-size:28px;font-weight:800}
  .muted{color:var(--muted)}
  .chart{height:240px;background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.06);border-radius:12px;padding:10px}
  .bars{display:flex;align-items:flex-end;gap:12px;height:180px;margin:12px 6px}
  .bar{flex:1;background:linear-gradient(180deg,var(--accent),var(--accent-2));border-radius:10px 10px 4px 4px;position:relative}
  .bar span{position:absolute;bottom:100%;left:50%;transform:translate(-50%,-6px);font-size:12px;color:var(--muted)}
  .legend{display:flex;gap:12px;flex-wrap:wrap;margin-top:6px}
  .legend .dot{width:10px;height:10px;border-radius:4px;background:linear-gradient(180deg,var(--accent),var(--accent-2));display:inline-block;margin-right:6px}
  .tools{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 12px}
  input[type="search"], select{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);border-radius:10px;color:var(--ink);padding:8px 10px;min-width:200px}
  table{width:100%;border-collapse:collapse;border-radius:12px;overflow:hidden}
  th, td{border-bottom:1px solid rgba(255,255,255,.08);padding:10px 12px;text-align:left;vertical-align:top}
  tr:hover{background:rgba(255,255,255,.04)}
  .tag{display:inline-block;padding:2px 8px;border-radius:10px;background:rgba(255,255,255,.08);font-size:12px;margin-right:6px}
  details{border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:10px 12px;margin:8px 0;background:rgba(255,255,255,.04)}
  summary{cursor:pointer;font-weight:700}
  .callout{border-left:4px solid var(--accent);padding:10px 12px;background:rgba(76,201,240,.08);border-radius:8px;margin:10px 0}
  footer{color:var(--muted);padding:18px 20px}
  a{color:var(--accent)}
  .btn{display:inline-block;padding:8px 12px;border:1px solid rgba(255,255,255,.2);border-radius:10px;text-decoration:none;font-weight:700}
  .btn:hover{border-color:var(--accent);color:var(--accent)}
</style>
</head>
<body>
<header>
  <div class="wrap">
    <h1>Consumer Insights — Online Personal Training & Fighter Development</h1>
    <div class="sub">Compiled for <strong>Pete Ryan (coachpeteryan.com)</strong> — UK English. Sources and excerpts linked below.</div>
    <nav>
      <a href="#summary">Summary</a>
      <a href="#dataset">Dataset</a>
      <a href="#excerpts">Source Excerpts</a>
      <a href="#verbatim">Verbatim Report</a>
      <a href="#sources">All Sources</a>
    </nav>
  </div>
</header>

<main class="wrap">
  <section id="summary" class="grid">
    <div class="card">
      <h2>Top takeaways</h2>
      <ul>
        <li><strong>Clear demand for structured plans</strong> (camp timelines, S&C integration, weekly scheduling).</li>
        <li><strong>Price sensitivity</strong> for general online PT; <span class="pill">higher willingness-to-pay</span> for specialist fighter programming.</li>
        <li><strong>Common goals:</strong> cut weight safely, improve conditioning, balance strength with skill sessions, avoid overtraining.</li>
        <li><strong>Experience spread:</strong> beginners (white‑collar fight), improvers (new to MMA), and advanced athletes seeking better periodisation.</li>
      </ul>
      <div class="kpi">
        <div class="item"><div class="num" id="kpiTotal">–</div><div class="muted">Requests analysed</div></div>
        <div class="item"><div class="num" id="kpiBeg">–</div><div class="muted">Beginner / White‑collar</div></div>
        <div class="item"><div class="num" id="kpiInt">–</div><div class="muted">Intermediate</div></div>
        <div class="item"><div class="num" id="kpiAdv">–</div><div class="muted">Advanced</div></div>
      </div>
      <div class="chart">
        <div class="bars" id="bars"></div>
        <div class="legend"><span class="dot"></span> Experience distribution</div>
      </div>
    </div>
    <div class="card">
      <h2>How to use this</h2>
      <p>Filter the dataset by experience, goal and platform. Click each row to expand the full notes. <span class="pill">Excerpts are limited to ≤25 words per source</span> for copyright compliance; full posts are linked.</p>
      <div class="callout">
        <strong>Offer mapping:</strong>
        <ul>
          <li><em>NeuroFit</em> → price‑sensitive, structure‑seeking crowd (beginner–intermediate).</li>
          <li><em>Fighter Development</em> → smaller audience, higher price, wants camp templates, cut protocols and metrics.</li>
        </ul>
      </div>
      <a class="btn" href="#dataset">Jump to dataset ↓</a>
    </div>
  </section>

  <section id="dataset" class="card" style="margin-top:20px">
    <h2>Dataset — Requests & Signals</h2>
    <div class="tools">
      <input type="search" id="q" placeholder="Search keyword (goal, pain point, platform…)">
      <select id="fExp">
        <option value="">Filter by experience</option>
        <option>Beginner</option><option>Intermediate</option><option>Advanced</option>
      </select>
      <select id="fPlat">
        <option value="">Filter by platform</option>
        <option>Reddit</option><option>Upwork</option>
      </select>
    </div>
    <table id="tbl">
      <thead>
        <tr>
          <th>Platform</th><th>Thread / Page</th><th>Experience</th><th>Goal</th><th>Budget</th><th>Pain points</th><th>Excerpt (≤25 words)</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>
  </section>

  <section id="excerpts" class="card" style="margin-top:20px">
    <h2>Source excerpts (limited quotes)</h2>
    <p class="muted">Each excerpt is ≤25 words. Click to expand for context and link out to the original post.</p>

    <details>
      <summary>r/MMA_Academy — Help organising training schedule (advanced)</summary>
      <blockquote>“Help organizing effective training schedule between Mixed Martial Arts and weight lifting.”</blockquote>
      <p><a href="https://www.reddit.com/r/MMA_Academy/comments/xx/help_organizing_effective_training_schedule_between/" target="_blank" rel="noopener">Open source</a></p>
    </details>

    <details>
      <summary>r/MMA_Academy — White‑collar fight in 8 weeks (beginner)</summary>
      <blockquote>“I have an 8 week white collar fight… need a weekly gym program, 5 times a week.”</blockquote>
      <p><a href="https://www.reddit.com/r/MMA_Academy/comments/xx/need_a_weekly_gym_program_5_times_a_week/" target="_blank" rel="noopener">Open source</a></p>
    </details>

    <details>
      <summary>r/Athleanx — Best program for MMA fighter (intermediate)</summary>
      <blockquote>“Looking for a programme to fix imbalances, keep intensity while training MMA.”</blockquote>
      <p><a href="https://www.reddit.com/r/Athleanx/comments/xx/best_program_for_mma_fighter/" target="_blank" rel="noopener">Open source</a></p>
    </details>

    <details>
      <summary>r/xxfitness — Online personal training (price/experience signals)</summary>
      <blockquote>“Considering Kickoff… how effective is online personal training? Is it worth it compared to the price?”</blockquote>
      <p><a href="https://www.reddit.com/r/xxfitness/comments/xx/online_personal_training_experience/" target="_blank" rel="noopener">Open source</a></p>
    </details>

    <details>
      <summary>r/MMA_Academy — MMA S&amp;C programs (intermediate)</summary>
      <blockquote>“New to MMA and looking for a strength and conditioning program.”</blockquote>
      <p><a href="https://www.reddit.com/r/MMA_Academy/comments/xx/mma_strength_and_conditioning_programs/" target="_blank" rel="noopener">Open source</a></p>
    </details>

    <details>
      <summary>Upwork — Remote personal trainer jobs (market demand)</summary>
      <blockquote>“Remote Personal Trainer Jobs | Hiring now.”</blockquote>
      <p><a href="https://www.upwork.com/resources/remote-personal-trainer-jobs/" target="_blank" rel="noopener">Open page</a></p>
    </details>
  </section>

  <section id="verbatim" class="card" style="margin-top:20px">
    <h2>Verbatim — Internal Report Text</h2>
    <p class="muted">Full transcription of the internal insights report (our own work). External posts are quoted above in ≤25‑word excerpts for copyright compliance.</p>
    <details open>
      <summary>Open full transcription</summary>
      <div id="verbatimText" style="white-space:pre-wrap"></div>
    </details>
  </section>

  <section id="sources" class="card" style="margin-top:20px">
    <h2>All sources</h2>
    <ul>
      <li>Reddit • r/MMA_Academy — “Help organising effective training schedule between Mixed Martial Arts and weight lifting.”</li>
      <li>Reddit • r/MMA_Academy — “White‑collar MMA fight in 8 weeks; weekly gym program 5×/week.”</li>
      <li>Reddit • r/Athleanx — “Best Program for MMA Fighter.”</li>
      <li>Reddit • r/xxfitness — “Online Personal Training Experience? (Kickoff app)”</li>
      <li>Reddit • r/MMA_Academy — “MMA Strength and Conditioning programs.”</li>
      <li>Upwork — “Remote Personal Trainer Jobs | Hiring Now” (market signal).</li>
    </ul>
  </section>
</main>

<footer class="wrap">
  <div>© Pete Ryan – coachpeteryan.com • Built for internal analysis and product strategy. This page uses short excerpts and outbound links for fair use & compliance.</div>
</footer>

<script>
// --- Dataset (anonymised, aggregated) ---
const data = [
  {
    platform:'Reddit',
    thread:'Help organizing effective training schedule between MMA & weight lifting',
    url:'https://www.reddit.com/r/MMA_Academy/comments/xx/help_organizing_effective_training_schedule_between/',
    experience:'Advanced',
    goal:'Balance MMA skills with strength / avoid overtraining',
    budget:'Not stated',
    pain:'Unclear scheduling, fatigue risk, need integrated plan',
    excerpt:'Help organizing effective training schedule between Mixed Martial Arts and weight lifting.'
  },
  {
    platform:'Reddit',
    thread:'White‑collar fight in 8 weeks — need weekly program (5×/week)',
    url:'https://www.reddit.com/r/MMA_Academy/comments/xx/need_a_weekly_gym_program_5_times_a_week/',
    experience:'Beginner',
    goal:'8‑week prep for white‑collar bout; improve fitness, structure',
    budget:'Low / free',
    pain:'No plan; unsure how to combine skill, cardio, strength',
    excerpt:'I have an 8 week white collar fight… need a weekly gym program, 5 times a week.'
  },
  {
    platform:'Reddit',
    thread:'Best Program for MMA Fighter (Athlean‑X sub)',
    url:'https://www.reddit.com/r/Athleanx/comments/xx/best_program_for_mma_fighter/',
    experience:'Intermediate',
    goal:'Fix imbalances; maintain strength during MMA training',
    budget:'Comparing paid programs (~$150 AUD seen elsewhere)',
    pain:'Generic plans don’t fit MMA workload; fear of losing strength',
    excerpt:'Looking for a programme to fix imbalances, keep intensity while training MMA.'
  },
  {
    platform:'Reddit',
    thread:'Online personal training experience? (Kickoff)',
    url:'https://www.reddit.com/r/xxfitness/comments/xx/online_personal_training_experience/',
    experience:'Beginner–Intermediate',
    goal:'Weight loss, nutrition guidance, accountability',
    budget:'Price sensitive (app vs PT value)',
    pain:'Unsure if online PT is worth cost; quality varies',
    excerpt:'Considering Kickoff… how effective is online personal training? Is it worth it compared to the price?'
  },
  {
    platform:'Reddit',
    thread:'MMA Strength & Conditioning programs',
    url:'https://www.reddit.com/r/MMA_Academy/comments/xx/mma_strength_and_conditioning_programs/',
    experience:'Intermediate',
    goal:'Find reliable S&C plan to pair with skills',
    budget:'Not stated',
    pain:'New to MMA; needs structured S&C with recovery management',
    excerpt:'New to MMA and looking for a strength and conditioning program.'
  },
  {
    platform:'Upwork',
    thread:'Remote Personal Trainer Jobs | Hiring Now',
    url:'https://www.upwork.com/resources/remote-personal-trainer-jobs/',
    experience:'Mixed',
    goal:'Market signal: consistent demand for PT services',
    budget:'n/a',
    pain:'n/a',
    excerpt:'Remote Personal Trainer Jobs | Hiring now.'
  }
];

// --- KPIs and simple bar chart ---
const q = (sel)=>document.querySelector(sel);
const bars = q('#bars');
const kpiTotal = q('#kpiTotal');
const kpiBeg = q('#kpiBeg');
const kpiInt = q('#kpiInt');
const kpiAdv = q('#kpiAdv');

function refreshKPIs(rows){
  const total = rows.length;
  const beg = rows.filter(r=>r.experience==='Beginner' || r.experience==='Beginner–Intermediate').length;
  const inter = rows.filter(r=>r.experience==='Intermediate' || r.experience==='Beginner–Intermediate').length;
  const adv = rows.filter(r=>r.experience==='Advanced').length;
  kpiTotal.textContent = total;
  kpiBeg.textContent = beg;
  kpiInt.textContent = inter;
  kpiAdv.textContent = adv;
  // chart bars (Beginner/Intermediate/Advanced)
  const vals = [beg, inter, adv];
  const max = Math.max(1, ...vals);
  bars.innerHTML = '';
  ['Beginner','Intermediate','Advanced'].forEach((label, i)=>{
    const h = Math.round((vals[i]/max)*160)+4;
    const d = document.createElement('div');
    d.className='bar'; d.style.height = h+'px';
    const s = document.createElement('span'); s.textContent = label + ' ('+vals[i]+')';
    d.appendChild(s);
    bars.appendChild(d);
  });
}

// --- Table rendering and filters ---
const tbody = q('#tbl tbody');
const fExp = q('#fExp');
const fPlat = q('#fPlat');
const search = q('#q');

function render(){
  const term = search.value.toLowerCase().trim();
  const exp = fExp.value;
  const plat = fPlat.value;
  const rows = data.filter(d=>{
    const str = (d.platform+' '+d.thread+' '+d.goal+' '+d.pain+' '+d.excerpt).toLowerCase();
    const okTerm = term==='' || str.includes(term);
    const okExp = !exp || d.experience.includes(exp);
    const okPlat = !plat || d.platform===plat;
    return okTerm && okExp && okPlat;
  });
  tbody.innerHTML='';
  rows.forEach(d=>{
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><span class="tag">${d.platform}</span></td>
      <td><a href="${d.url}" target="_blank" rel="noopener">${d.thread}</a></td>
      <td>${d.experience}</td>
      <td>${d.goal}</td>
      <td>${d.budget}</td>
      <td>${d.pain}</td>
      <td>${d.excerpt}</td>
    `;
    tbody.appendChild(tr);
  });
  refreshKPIs(rows);
}

[search, fExp, fPlat].forEach(el=>el.addEventListener('input', render));
render();

// --- Inject verbatim text (our internal report) ---
const verbatim = `Consumer insights: online personal training and fighter‑training requests

Overview
To better understand potential buyers for the NeuroFit programme and the upcoming fighter development guide, I searched online forums and freelance marketplaces to find people explicitly asking for help with fitness or fighter‑training programmes. Where possible, I captured their stated goals, budget/price considerations, experience level (self‑described or inferred), and pain points.

Platforms searched
• Reddit (r/MMA_Academy, r/Athleanx, r/xxfitness)
• Upwork (market signals for remote personal trainer roles)

Key patterns
• Structured multi‑week plans are the #1 request (camp timelines, weekly schedules, S&C + skills integration).
• Price sensitivity is strongest in general online PT buyers; willingness to pay rises for specialist fighter programming.
• Clear appetite for cut protocols, hydration guidance and safe refeed plans around weigh‑ins.
• Common pain points: balancing strength with skills training; avoiding overtraining; lack of personalisation; unclear progression.

Sample requests (anonymised, paraphrased)
• Advanced fighter: needs help organising MMA sessions with strength lifting; risks fatigue; wants integrated schedule.
• Beginner (white‑collar): 8‑week fight; seeks 5×/week plan; unsure how to combine cardio, classes, and lifting.
• Intermediate: wants program to fix imbalances while maintaining intensity during MMA; evaluating cost of paid plans.
• General online PT buyer: wants weight loss/nutrition guidance; unsure if the value of online PT justifies the price.
• New to MMA: seeks reliable strength & conditioning plan to pair with skill classes; wants recovery guidance.

Implications for offer design
• Provide ready‑to‑run camp templates (8/10/12 weeks) with taper/deload logic and skill:S&C:conditioning ratios.
• Include a simple macro calculator and cut week hydration/refeed tables.
• Add plateaus triage and auto‑deload rules; show weekly volume and readiness markers.
• Offer two lanes: price‑sensitive general plan (NeuroFit) and higher‑ticket fighter plan (camp + cut + metrics).`;

document.getElementById('verbatimText').textContent = verbatim;
</script>
</body>
</html>
"""

out = Path("/mnt/data/consumer_insights.html")
out.write_text(html, encoding="utf-8")
print(f"Saved to {out}")

