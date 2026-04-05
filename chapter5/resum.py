<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Enhanced Glass Resume Builder — Samarth</title>

<!-- html2pdf for PDF export -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.3/html2pdf.bundle.min.js"></script>

<style>
  :root{
    --bg: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(245,249,255,0.7), rgba(240,240,255,0.6));
    --card-bg: rgba(255,255,255,0.4);
    --glass-border: rgba(255,255,255,0.7);
    --accent: #0ea5e9;
    --text: #0f172a;
    --muted: #475569;
    --glass-blur: 12px;
    --shadow: 0 10px 40px rgba(15,23,42,0.1);
  }

  body.dark { 
    --bg: linear-gradient(135deg,#0b1220,#071022,#0a0e1a); 
    --card-bg: rgba(255,255,255,0.04); 
    --glass-border: rgba(255,255,255,0.06); 
    --text:#e6eef8; 
    --muted:#94a3b8; 
    --shadow: 0 10px 40px rgba(2,6,23,0.8); 
  }
  
  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes slideIn { from { opacity: 0; transform: translateX(-20px); } to { opacity: 1; transform: translateX(0); } }

  *{box-sizing:border-box}
  html,body{height:100%;margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial;}
  body{background:var(--bg);color:var(--text);padding:28px;transition:background .3s,color .3s;animation:fadeIn 0.5s ease-out;overflow-x:hidden}
  body::before{content:'';position:fixed;top:0;left:0;right:0;bottom:0;background:radial-gradient(circle at 20% 20%, rgba(14,165,233,0.08) 0%, transparent 50%), radial-gradient(circle at 80% 80%, rgba(125,211,252,0.08) 0%, transparent 50%);pointer-events:none;z-index:0}
  .app{max-width:1300px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start;position:relative;z-index:1}

  /* header controls */
  .topbar{display:flex;gap:12px;align-items:center;justify-content:space-between;margin-bottom:20px;animation:slideIn 0.6s ease-out;position:relative;z-index:1;flex-wrap:wrap}
  .controls{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
  .btn{background:var(--accent);color:white;padding:10px 16px;border-radius:12px;border:none;cursor:pointer;font-weight:600;box-shadow:var(--shadow);display:inline-flex;gap:8px;align-items:center;transition:all .3s ease;position:relative;overflow:hidden;font-size:14px}
  .btn:hover{transform:translateY(-2px);box-shadow:0 12px 50px rgba(14,165,233,0.3)}
  .btn:active{transform:translateY(0)}
  .btn.secondary{background:var(--card-bg);color:var(--text);border:1px solid var(--glass-border);backdrop-filter:blur(8px)}
  .btn.secondary:hover{background:rgba(255,255,255,0.5);border-color:var(--accent)}
  body.dark .btn.secondary:hover{background:rgba(255,255,255,0.08)}
  .icon{width:18px;height:18px;display:inline-block}
  .kbd{display:inline-block;padding:2px 6px;background:rgba(0,0,0,0.05);border-radius:4px;font-size:11px;font-family:monospace;margin-left:6px}

  /* left editor */
  .editor{padding:24px;border-radius:20px;background:var(--card-bg);backdrop-filter: blur(var(--glass-blur));border:1px solid var(--glass-border);box-shadow:var(--shadow);min-height:72vh;overflow:auto;animation:fadeIn 0.7s ease-out 0.1s both;transition:all .3s ease}
  .editor:hover{box-shadow:0 15px 60px rgba(15,23,42,0.15)}
  body.dark .editor:hover{box-shadow:0 15px 60px rgba(2,6,23,0.9)}
  
  .section-form{margin-bottom:20px;padding:16px;border-radius:16px;background:linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.03));border:1px solid rgba(255,255,255,0.1);transition:all .3s ease;position:relative}
  .section-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;cursor:move;padding:8px;margin:-8px -8px 12px;border-radius:8px;transition:background .2s}
  .section-header h3{margin:0;font-size:16px;font-weight:700;color:var(--accent);display:flex;align-items:center;gap:8px}
  .drag-handle{cursor:grab;color:var(--muted);font-size:18px;user-select:none}
  
  label{display:block;font-size:13px;color:var(--muted);margin-bottom:8px;font-weight:500;letter-spacing:0.3px}
  input[type="text"], input[type="email"], input[type="url"], textarea, select{width:100%;padding:12px;border-radius:12px;border:1px solid rgba(0,0,0,0.08);font-size:14px;background:rgba(255,255,255,0.5);color:var(--text);transition:all .3s ease;backdrop-filter:blur(4px)}
  body.dark input[type="text"], body.dark input[type="email"], body.dark input[type="url"], body.dark textarea, body.dark select{background:rgba(255,255,255,0.03);border-color:rgba(255,255,255,0.06)}
  input:focus, textarea:focus, select:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(14,165,233,0.1);transform:translateY(-1px)}
  textarea{min-height:90px;resize:vertical;font-family:inherit}
  .row{display:flex;gap:12px}
  .col{flex:1}

  /* right preview (resume) */
  .preview-wrap{padding:24px;border-radius:20px;background:linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.08));backdrop-filter: blur(8px);border:1px solid rgba(255,255,255,0.4);min-height:72vh;overflow:auto;position:relative;animation:fadeIn 0.7s ease-out 0.2s both;transition:all .3s ease}
  .preview-wrap:hover{box-shadow:0 15px 60px rgba(15,23,42,0.15)}
  body.dark .preview-wrap:hover{box-shadow:0 15px 60px rgba(2,6,23,0.9)}
  
  .resume{max-width:820px;margin:0 auto;background:rgba(255,255,255,0.92);padding:32px;border-radius:16px;border:1px solid rgba(255,255,255,0.7);box-shadow:0 5px 25px rgba(0,0,0,0.05);transition:all .3s ease}
  body.dark .resume{background: linear-gradient(135deg, rgba(3,7,18,0.9), rgba(6,10,22,0.95)); color:var(--text);border-color:rgba(255,255,255,0.08)}
  
  .resume-head{display:flex;gap:20px;align-items:center;margin-bottom:24px;padding-bottom:20px;border-bottom:2px solid rgba(0,0,0,0.05);position:relative}
  body.dark .resume-head{border-bottom-color:rgba(255,255,255,0.08)}
  
  .avatar{width:100px;height:100px;border-radius:16px;background:linear-gradient(135deg,var(--accent),#7dd3fc);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:28px;border:4px solid rgba(255,255,255,0.95);box-shadow:0 8px 25px rgba(14,165,233,0.25);transition:transform .3s ease}
  .avatar:hover{transform:scale(1.05) rotate(2deg)}
  
  .name{font-size:28px;font-weight:800;margin-bottom:4px;background:linear-gradient(135deg,var(--text),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
  .meta{color:var(--muted);font-size:14px;margin-top:4px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
  .meta-item{display:inline-flex;align-items:center;gap:6px}
  
  .section-title{color:var(--accent);font-weight:700;margin-top:20px;margin-bottom:12px;font-size:16px;text-transform:uppercase;letter-spacing:1px;display:flex;align-items:center;gap:8px}
  .section-title::before{content:'';width:4px;height:16px;background:var(--accent);border-radius:2px}

  /* skills */
  .skill{display:flex;align-items:center;gap:10px;margin-bottom:8px}
  .skill .bar{flex:1;height:10px;background:rgba(0,0,0,0.06);border-radius:999px;overflow:hidden}
  body.dark .skill .bar{background:rgba(255,255,255,0.06)}
  .skill .fill{height:100%;background:linear-gradient(90deg,var(--accent),#7dd3fc);transition:width .3s ease}

  /* social links */
  .social-links{display:flex;gap:12px;flex-wrap:wrap;margin-top:12px}
  .social-link{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:10px;background:linear-gradient(135deg, rgba(14,165,233,0.1), rgba(125,211,252,0.05));border:1px solid rgba(14,165,233,0.2);color:var(--accent);font-size:13px;font-weight:600;text-decoration:none;transition:all .3s ease}
  .social-link:hover{background:linear-gradient(135deg, rgba(14,165,233,0.2), rgba(125,211,252,0.1));transform:translateY(-2px);box-shadow:0 4px 15px rgba(14,165,233,0.2)}

  /* dynamic list UI */
  .small{font-size:13px;color:var(--muted)}
  .add-row{display:flex;gap:10px;align-items:center;margin-top:8px;flex-wrap:wrap}
  .chip{display:inline-flex;padding:6px 10px;border-radius:999px;background:linear-gradient(90deg,var(--accent),#7dd3fc);color:#fff;font-size:13px;margin:6px 6px 0 0;transition:transform .2s}
  .chip:hover{transform:scale(1.05)}

  /* item cards */
  .item-card{border:1px dashed rgba(0,0,0,0.06);border-radius:12px;padding:12px;margin-bottom:12px;background:rgba(255,255,255,0.3);backdrop-filter:blur(4px);transition:all .3s ease}
  body.dark .item-card{background:rgba(255,255,255,0.02);border-color:rgba(255,255,255,0.06)}
  .item-card:hover{border-color:var(--accent);background:rgba(255,255,255,0.5);transform:translateX(4px)}
  body.dark .item-card:hover{background:rgba(255,255,255,0.04)}
  
  .item-actions{display:flex;gap:8px;margin-top:10px;justify-content:flex-end}

  /* file input hidden */
  input[type=file]{display:none}

  /* toast */
  .toast{position:fixed;right:24px;bottom:24px;background:var(--accent);color:#fff;padding:14px 18px;border-radius:12px;box-shadow:0 10px 40px rgba(14,165,233,0.3);display:none;align-items:center;gap:10px;z-index:1000;animation:slideIn 0.3s ease-out;font-weight:600}

  /* modal */
  .modal{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.5);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:1000;animation:fadeIn 0.3s ease-out}
  .modal-content{background:var(--card-bg);backdrop-filter:blur(var(--glass-blur));border:1px solid var(--glass-border);border-radius:20px;padding:28px;max-width:600px;width:90%;max-height:80vh;overflow:auto;box-shadow:var(--shadow);animation:fadeIn 0.4s ease-out}
  .modal-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
  .modal-header h2{margin:0;font-size:22px;color:var(--accent)}
  .modal-close{background:none;border:none;font-size:28px;cursor:pointer;color:var(--muted);padding:0;width:32px;height:32px;display:flex;align-items:center;justify-content:center;border-radius:8px;transition:all .2s}
  .modal-close:hover{background:rgba(0,0,0,0.05);color:var(--text)}

  /* responsive */
  @media (max-width:1000px){
    .app{grid-template-columns:1fr; padding-bottom:40px}
    .preview-wrap{order:2}
    .editor{order:1}
    .topbar{flex-direction:column;align-items:flex-start}
    .controls{width:100%}
  }

  /* template variations */
  body.template-classic .resume{font-family:Georgia,serif;padding:40px}
  body.template-classic .name{font-family:Georgia,serif}
  body.template-minimal .resume{padding:24px;border:none}
  body.template-minimal .section-title{text-transform:none;font-size:14px;letter-spacing:0}
  body.template-minimal .section-title::before{display:none}
</style>
</head>
<body>
  <div class="topbar">
    <div>
      <strong style="font-size:20px;background:linear-gradient(135deg,var(--accent),#7dd3fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">✨ Glass Resume Builder Pro</strong>
      <div class="small" style="margin-top:4px">AI-powered • Live preview • Multiple exports • Drag & drop</div>
    </div>

    <div class="controls">
      <div style="display:flex;gap:8px;align-items:center">
        <label class="small" style="font-weight:600">Accent</label>
        <input id="accentColor" type="color" value="#0ea5e9" title="Accent color" style="cursor:pointer;width:40px;height:32px;border:none;border-radius:8px">
      </div>

      <div class="history-controls">
        <button class="btn secondary" id="undoBtn" title="Undo (Ctrl+Z)">↶</button>
        <button class="btn secondary" id="redoBtn" title="Redo (Ctrl+Y)">↷</button>
      </div>

      <button class="btn secondary" id="templateBtn">🎨 Templates</button>
      <button class="btn secondary" id="aiBtn">✨ AI Suggest</button>
      <button class="btn" id="saveBtn" title="Save (Ctrl+S)">💾 Save</button>
      <button class="btn secondary" id="importBtn">📥 Import</button>
      <button class="btn secondary" id="exportJsonBtn">📤 Export</button>
      <button class="btn secondary" id="downloadDoc">DOC</button>
      <button class="btn" id="downloadPdf" title="Export PDF (Ctrl+P)">PDF</button>
      <button class="btn secondary" id="toggleTheme">🌙</button>
      <label class="btn secondary" for="photoUpload">📷 Photo</label>
      <input type="file" id="photoUpload" accept="image/*">
      <input type="file" id="importJsonFile" accept="application/json" style="display:none">
    </div>
  </div>

  <div class="app">
    <!-- EDITOR -->
    <div class="editor" id="editor">

      <!-- Personal -->
      <div class="section-form" data-section="personal">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Personal Information</h3>
        </div>
        
        <label>Full Name</label>
        <input id="fullName" type="text" placeholder="e.g. Samarth Jain" spellcheck="true">

        <div class="row" style="margin-top:10px">
          <div class="col">
            <label>Email</label>
            <input id="email" type="email" placeholder="you@example.com">
          </div>
          <div class="col">
            <label>Phone</label>
            <input id="phone" type="text" placeholder="+91 9xx xxx xxxx">
          </div>
        </div>

        <label style="margin-top:10px">Professional Title</label>
        <input id="title" type="text" placeholder="AI Engineering Student / Generative AI">

        <label style="margin-top:10px">Location</label>
        <input id="location" type="text" placeholder="Indore, India">

        <label style="margin-top:10px">Summary</label>
        <textarea id="summary" placeholder="Short professional summary highlighting your expertise and goals..." spellcheck="true"></textarea>

        <div style="margin-top:12px;display:flex;gap:10px;align-items:center;justify-content:space-between;flex-wrap:wrap">
          <div class="small" id="wordCount">Words: 0</div>
          <div style="display:flex;gap:8px;align-items:center">
            <button class="btn secondary" id="resetBtn">🔄 Reset</button>
            <button class="btn secondary" id="clearPhoto">Clear Photo</button>
          </div>
        </div>
      </div>

      <!-- Social Links -->
      <div class="section-form" data-section="social">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Social Links</h3>
        </div>
        
        <div class="row">
          <div class="col">
            <label>LinkedIn</label>
            <input id="linkedin" type="url" placeholder="https://linkedin.com/in/yourname">
          </div>
          <div class="col">
            <label>GitHub</label>
            <input id="github" type="url" placeholder="https://github.com/yourname">
          </div>
        </div>
        
        <div class="row" style="margin-top:10px">
          <div class="col">
            <label>Portfolio</label>
            <input id="portfolio" type="url" placeholder="https://yourportfolio.com">
          </div>
          <div class="col">
            <label>Twitter/X</label>
            <input id="twitter" type="url" placeholder="https://twitter.com/yourname">
          </div>
        </div>
      </div>

      <!-- Skills -->
      <div class="section-form" data-section="skills">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Skills</h3>
        </div>
        <div id="skillsList"></div>
        <div class="add-row">
          <input id="newSkill" type="text" placeholder="Add skill (e.g. PyTorch)">
          <select id="skillLevel">
            <option value="95">Expert</option>
            <option value="85">Advanced</option>
            <option value="70">Intermediate</option>
            <option value="50">Beginner</option>
          </select>
          <button class="btn" id="addSkill">+ Add</button>
        </div>
      </div>

      <!-- Experience -->
      <div class="section-form" data-section="experience">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Experience</h3>
        </div>
        <div id="expList"></div>
        <div class="add-row">
          <button class="btn secondary" id="addExperience">+ Add Experience</button>
        </div>
      </div>

      <!-- Education -->
      <div class="section-form" data-section="education">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Education</h3>
        </div>
        <div id="eduList"></div>
        <div class="add-row">
          <button class="btn secondary" id="addEducation">+ Add Education</button>
        </div>
      </div>

      <!-- Projects -->
      <div class="section-form" data-section="projects">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Projects</h3>
        </div>
        <div id="projList"></div>
        <div class="add-row">
          <button class="btn secondary" id="addProject">+ Add Project</button>
        </div>
      </div>

      <!-- Languages -->
      <div class="section-form" data-section="languages">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Languages</h3>
        </div>
        <div id="langList"></div>
        <div class="add-row">
          <input id="newLang" type="text" placeholder="Language (e.g. English)">
          <select id="langLevel">
            <option value="Native">Native</option>
            <option value="Fluent">Fluent</option>
            <option value="Professional">Professional</option>
            <option value="Intermediate">Intermediate</option>
            <option value="Basic">Basic</option>
          </select>
          <button class="btn" id="addLang">+ Add</button>
        </div>
      </div>

      <!-- Certifications -->
      <div class="section-form" data-section="certifications">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Certifications</h3>
        </div>
        <div id="certList"></div>
        <div class="add-row">
          <input id="newCert" type="text" placeholder="Add certification (Coursera - DeepLearning.AI)" style="flex:1">
          <button class="btn" id="addCert">+ Add</button>
        </div>
      </div>

      <!-- Custom Sections -->
      <div class="section-form" data-section="custom">
        <div class="section-header">
          <h3><span class="drag-handle">⋮⋮</span> Custom Sections</h3>
        </div>
        <div id="customSections"></div>
        <div class="add-row">
          <input id="newCustomTitle" type="text" placeholder="Section title (e.g. Awards, Publications)">
          <button class="btn" id="addCustomSection">+ Add Section</button>
        </div>
      </div>

      <div style="margin-top:16px;color:var(--muted);font-size:13px;line-height:1.6">
        <strong>💡 Tips:</strong> Auto-saves every change. Use <span class="kbd">Ctrl+S</span> to force save (auto-download PDF). 
        <span class="kbd">Ctrl+Z</span> to undo. <span class="kbd">Ctrl+P</span> to export PDF.
      </div>
    </div>

    <!-- PREVIEW -->
    <div class="preview-wrap" id="previewWrap">
      <div id="previewInner" class="resume" spellcheck="false">
        <div class="resume-head">
          <div class="avatar" id="previewAvatar">SJ</div>
          <div style="flex:1">
            <div class="name" id="previewName">Samarth Jain</div>
            <div class="meta" id="previewTitle">AI Engineering Student</div>
            <div class="meta" id="previewContact"></div>
            <div id="previewSocial" class="social-links"></div>
          </div>
        </div>

        <div id="previewSummary" style="margin-bottom:12px;line-height:1.7"></div>

        <div id="previewSkills"></div>
        <div id="previewExp"></div>
        <div id="previewEdu"></div>
        <div id="previewProjects"></div>
        <div id="previewLangs"></div>
        <div id="previewCerts"></div>
        <div id="previewCustom"></div>
      </div>
    </div>
  </div>

  <div class="toast" id="toast">Saved ✓</div>

  <!-- Template Modal -->
  <div class="modal" id="templateModal">
    <div class="modal-content">
      <div class="modal-header">
        <h2>Choose Template</h2>
        <button class="modal-close" id="closeTemplate">×</button>
      </div>
      <div class="template-grid">
        <div class="template-card active" data-template="modern">
          <div style="font-size:32px;margin-bottom:8px">🎨</div>
          <strong>Modern</strong>
          <div class="small">Glassmorphism style</div>
        </div>
        <div class="template-card" data-template="minimal">
          <div style="font-size:32px;margin-bottom:8px">🧾</div>
          <strong>Minimal</strong>
          <div class="small">Clean, no borders</div>
        </div>
        <div class="template-card" data-template="classic">
          <div style="font-size:32px;margin-bottom:8px">🏛️</div>
          <strong>Classic</strong>
          <div class="small">Serif, printable</div>
        </div>
      </div>
    </div>
  </div>

<script>
/*
  Complete functionality implemented:
  - State stored in `state`
  - Auto-save to localStorage
  - Save button triggers PDF download (user chose B)
  - Import / Export JSON
  - Download DOC
  - Undo/Redo stack
  - Live preview
  - Photo upload
  - Add/remove items for lists
*/

const STORAGE_KEY = 'glass_resume_v1';
const UNDO_LIMIT = 40;

// default state
const defaultState = {
  personal: {
    fullName: 'Samarth Jain',
    email: '',
    phone: '',
    title: 'AI Engineering Student',
    location: 'Indore, India',
    summary: 'AI engineering student with interests in generative models, ML engineering, and applied research.',
    avatarDataUrl: null
  },
  social: { linkedin:'', github:'', portfolio:'', twitter:'' },
  skills: [{name:'Python', level:95},{name:'PyTorch', level:85}],
  experience: [],
  education: [],
  projects: [],
  languages: [],
  certs: [],
  custom: [],
  template: 'modern',
  theme: localStorage.getItem('theme') || 'light',
  accent: '#0ea5e9'
};

// in-memory state & history
let state = {};
let historyStack = [];
let historyIndex = -1;

// element refs
const els = {
  fullName: document.getElementById('fullName'),
  email: document.getElementById('email'),
  phone: document.getElementById('phone'),
  title: document.getElementById('title'),
  location: document.getElementById('location'),
  summary: document.getElementById('summary'),
  wordCount: document.getElementById('wordCount'),
  linkedin: document.getElementById('linkedin'),
  github: document.getElementById('github'),
  portfolio: document.getElementById('portfolio'),
  twitter: document.getElementById('twitter'),
  skillsList: document.getElementById('skillsList'),
  addSkillBtn: document.getElementById('addSkill'),
  newSkill: document.getElementById('newSkill'),
  skillLevel: document.getElementById('skillLevel'),
  expList: document.getElementById('expList'),
  eduList: document.getElementById('eduList'),
  projList: document.getElementById('projList'),
  langList: document.getElementById('langList'),
  certList: document.getElementById('certList'),
  customSections: document.getElementById('customSections'),
  newLang: document.getElementById('newLang'),
  langLevel: document.getElementById('langLevel'),
  newCert: document.getElementById('newCert'),
  newCustomTitle: document.getElementById('newCustomTitle'),
  addLang: document.getElementById('addLang'),
  addCert: document.getElementById('addCert'),
  addCustomSection: document.getElementById('addCustomSection'),
  addExperience: document.getElementById('addExperience'),
  addEducation: document.getElementById('addEducation'),
  addProject: document.getElementById('addProject'),
  previewName: document.getElementById('previewName'),
  previewTitle: document.getElementById('previewTitle'),
  previewContact: document.getElementById('previewContact'),
  previewSocial: document.getElementById('previewSocial'),
  previewAvatar: document.getElementById('previewAvatar'),
  previewSummary: document.getElementById('previewSummary'),
  previewSkills: document.getElementById('previewSkills'),
  previewExp: document.getElementById('previewExp'),
  previewEdu: document.getElementById('previewEdu'),
  previewProjects: document.getElementById('previewProjects'),
  previewLangs: document.getElementById('previewLangs'),
  previewCerts: document.getElementById('previewCerts'),
  previewCustom: document.getElementById('previewCustom'),
  saveBtn: document.getElementById('saveBtn'),
  downloadPdf: document.getElementById('downloadPdf'),
  downloadDoc: document.getElementById('downloadDoc'),
  exportJsonBtn: document.getElementById('exportJsonBtn'),
  importBtn: document.getElementById('importBtn'),
  importJsonFile: document.getElementById('importJsonFile'),
  photoUpload: document.getElementById('photoUpload'),
  clearPhoto: document.getElementById('clearPhoto'),
  toast: document.getElementById('toast'),
  undoBtn: document.getElementById('undoBtn'),
  redoBtn: document.getElementById('redoBtn'),
  toggleTheme: document.getElementById('toggleTheme'),
  accentColor: document.getElementById('accentColor'),
  resetBtn: document.getElementById('resetBtn'),
  templateBtn: document.getElementById('templateBtn'),
  templateModal: document.getElementById('templateModal'),
  closeTemplate: document.getElementById('closeTemplate'),
  templateGrid: document.querySelector('.template-grid')
};

// helpers
function showToast(msg='Saved ✓', ms=1800){
  els.toast.textContent = msg;
  els.toast.style.display = 'flex';
  setTimeout(()=>{ els.toast.style.display='none'; }, ms);
}

function deepClone(obj){ return JSON.parse(JSON.stringify(obj)); }

// history (undo/redo)
function pushHistory() {
  // trim forward history if we branched
  if(historyIndex < historyStack.length - 1) {
    historyStack = historyStack.slice(0, historyIndex+1);
  }
  historyStack.push(deepClone(state));
  if(historyStack.length > UNDO_LIMIT) historyStack.shift();
  historyIndex = historyStack.length - 1;
  updateUndoRedoButtons();
}
function undo(){
  if(historyIndex <= 0) return;
  historyIndex--;
  state = deepClone(historyStack[historyIndex]);
  persistState(false); // update UI
  renderAll();
  updateUndoRedoButtons();
}
function redo(){
  if(historyIndex >= historyStack.length - 1) return;
  historyIndex++;
  state = deepClone(historyStack[historyIndex]);
  persistState(false);
  renderAll();
  updateUndoRedoButtons();
}
function updateUndoRedoButtons(){
  els.undoBtn.disabled = historyIndex <= 0;
  els.redoBtn.disabled = historyIndex >= historyStack.length - 1;
}

// persist state to localStorage
function persistState(silent=true){
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  if(!silent) showToast('Saved ✓');
}

// load from storage or default
function loadState(){
  const raw = localStorage.getItem(STORAGE_KEY);
  if(raw){
    try{
      state = JSON.parse(raw);
      // merge missing defaults
      state = Object.assign(deepClone(defaultState), state);
    }catch(e){
      state = deepClone(defaultState);
    }
  } else {
    state = deepClone(defaultState);
  }
  // apply theme accent
  document.documentElement.style.setProperty('--accent', state.accent || defaultState.accent);
  if(state.theme === 'dark') document.body.classList.add('dark'); else document.body.classList.remove('dark');
  els.accentColor.value = state.accent || defaultState.accent;
  els.accentColor.addEventListener('input', e=>{
    const v = e.target.value;
    document.documentElement.style.setProperty('--accent', v);
    state.accent = v;
    pushHistory(); persistState(true);
  });
}

// rendering
function renderAll(){
  // personal fields
  const p = state.personal;
  els.fullName.value = p.fullName || '';
  els.email.value = p.email || '';
  els.phone.value = p.phone || '';
  els.title.value = p.title || '';
  els.location.value = p.location || '';
  els.summary.value = p.summary || '';
  updateWordCount();
  // social
  els.linkedin.value = state.social.linkedin || '';
  els.github.value = state.social.github || '';
  els.portfolio.value = state.social.portfolio || '';
  els.twitter.value = state.social.twitter || '';

  // lists
  renderSkills();
  renderExp();
  renderEdu();
  renderProjects();
  renderLangs();
  renderCerts();
  renderCustom();

  // preview
  renderPreview();
}

function renderPreview(){
  const p = state.personal;
  els.previewName.textContent = p.fullName || 'Your Name';
  els.previewTitle.textContent = p.title || '';
  const contactParts = [];
  if(p.email) contactParts.push(p.email);
  if(p.phone) contactParts.push(p.phone);
  if(p.location) contactParts.push(p.location);
  els.previewContact.innerHTML = contactParts.map(x=>`<span class="meta-item">${x}</span>`).join('');
  // social
  els.previewSocial.innerHTML = '';
  const social = state.social;
  Object.entries(social).forEach(([k,v])=>{
    if(v && v.trim()){
      const a = document.createElement('a');
      a.href = v; a.target='_blank'; a.rel='noopener';
      a.className='social-link';
      a.textContent = k.charAt(0).toUpperCase()+k.slice(1);
      els.previewSocial.appendChild(a);
    }
  });
  // avatar
  if(p.avatarDataUrl){
    els.previewAvatar.style.backgroundImage = `url('${p.avatarDataUrl}')`;
    els.previewAvatar.style.backgroundSize = 'cover';
    els.previewAvatar.textContent = '';
  } else {
    els.previewAvatar.style.backgroundImage = 'none';
    const initials = (p.fullName || 'SJ').split(' ').map(s=>s[0]).slice(0,2).join('').toUpperCase();
    els.previewAvatar.textContent = initials || 'SJ';
  }
  // summary
  els.previewSummary.textContent = p.summary || '';

  // skills
  els.previewSkills.innerHTML = '';
  if(state.skills.length){
    const title = el('h4', {className:'section-title'}, 'Skills');
    els.previewSkills.appendChild(title);
    state.skills.forEach(s=>{
      const wrapper = document.createElement('div');
      wrapper.className = 'skill';
      wrapper.innerHTML = `<div style="min-width:110px;font-weight:600">${escapeHtml(s.name)}</div>
        <div class="bar"><div class="fill" style="width:${+s.level}%"></div></div>`;
      els.previewSkills.appendChild(wrapper);
    });
  }

  // experience
  els.previewExp.innerHTML = '';
  if(state.experience.length){
    els.previewExp.appendChild(el('div',{className:'section-title'}, 'Experience'));
    state.experience.forEach(item=>{
      const card = el('div',{className:'item-card'}, 
        el('div',{style:'font-weight:700'}, item.role || ''),
        el('div',{className:'small'}, `${item.company || ''} • ${item.period || ''}`),
        el('div',{}, item.description || '')
      );
      els.previewExp.appendChild(card);
    });
  }

  // education
  els.previewEdu.innerHTML = '';
  if(state.education.length){
    els.previewEdu.appendChild(el('div',{className:'section-title'}, 'Education'));
    state.education.forEach(item=>{
      els.previewEdu.appendChild(el('div',{className:'item-card'}, 
        el('div',{style:'font-weight:700'}, item.degree || ''),
        el('div',{className:'small'}, `${item.school || ''} • ${item.year || ''}`),
        el('div',{}, item.description || '')
      ));
    });
  }

  // projects
  els.previewProjects.innerHTML = '';
  if(state.projects.length){
    els.previewProjects.appendChild(el('div',{className:'section-title'}, 'Projects'));
    state.projects.forEach(item=>{
      els.previewProjects.appendChild(el('div',{className:'item-card'}, 
        el('div',{style:'font-weight:700'}, item.title || ''),
        el('div',{className:'small'}, item.link ? `<a href="${escapeHtmlAttr(item.link)}" target="_blank" rel="noopener">${escapeHtml(item.link)}</a>` : ''),
        el('div',{}, item.description || '')
      ));
    });
  }

  // languages
  els.previewLangs.innerHTML = '';
  if(state.languages.length){
    els.previewLangs.appendChild(el('div',{className:'section-title'}, 'Languages'));
    state.languages.forEach(l=>{
      els.previewLangs.appendChild(el('div',{className:'item-card'}, `${escapeHtml(l.name)} — <strong>${escapeHtml(l.level)}</strong>`));
    });
  }

  // certs
  els.previewCerts.innerHTML = '';
  if(state.certs.length){
    els.previewCerts.appendChild(el('div',{className:'section-title'}, 'Certifications'));
    state.certs.forEach(c=>{
      els.previewCerts.appendChild(el('div',{className:'item-card'}, `${escapeHtml(c)}`));
    });
  }

  // custom
  els.previewCustom.innerHTML = '';
  if(state.custom.length){
    state.custom.forEach(csec=>{
      const title = el('div',{className:'section-title'}, escapeHtml(csec.title || ''));
      els.previewCustom.appendChild(title);
      if(csec.items && csec.items.length){
        csec.items.forEach(it=>{
          els.previewCustom.appendChild(el('div',{className:'item-card'}, escapeHtml(it)));
        });
      }
    });
  }
}

// small utility to create elements
function el(tag, attrsOrText, maybeText){
  const e = document.createElement(tag);
  if(typeof attrsOrText === 'object' && attrsOrText !== null && !Array.isArray(attrsOrText)){
    Object.entries(attrsOrText).forEach(([k,v])=>{
      if(k==='className') e.className = v;
      else if(k==='style') e.style.cssText = v;
      else e.setAttribute(k, v);
    });
    if(maybeText) e.innerHTML = maybeText;
  } else {
    e.innerHTML = attrsOrText || '';
  }
  return e;
}

// escape helpers
function escapeHtml(s){ if(!s) return ''; return String(s).replace(/[&<>"']/g, function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]; });}
function escapeHtmlAttr(s){ return escapeHtml(s); }

// Rendering list editors
function renderSkills(){
  els.skillsList.innerHTML = '';
  state.skills.forEach((s, idx)=>{
    const card = el('div',{className:'item-card'});
    const row = el('div',{className:'row'});
    const col1 = el('div',{className:'col'}, `<label style="font-weight:700">${escapeHtml(s.name)}</label><div class="small">Level: ${s.level}%</div>`);
    const actions = el('div',{className:'item-actions'});
    const del = el('button',{className:'btn secondary'}, 'Remove');
    del.onclick = ()=>{ state.skills.splice(idx,1); pushHistory(); persistState(true); renderSkills(); renderPreview(); };
    actions.appendChild(del);
    card.appendChild(row);
    card.appendChild(col1);
    card.appendChild(actions);
    els.skillsList.appendChild(card);
  });
}
function renderExp(){
  els.expList.innerHTML = '';
  state.experience.forEach((it, idx)=>{
    const card = el('div',{className:'item-card'});
    const role = el('input',{type:'text', placeholder:'Role', value:it.role || ''});
    const company = el('input',{type:'text', placeholder:'Company', value:it.company || ''});
    const period = el('input',{type:'text', placeholder:'Period (e.g. 2023 - Present)', value:it.period || ''});
    const desc = document.createElement('textarea'); desc.placeholder='Description'; desc.value = it.description || '';
    [role, company, period, desc].forEach(x=>{ x.style.width='100%'; x.style.marginBottom='8px'; });
    role.addEventListener('input', ()=>{ it.role=role.value; pushHistory(); persistState(true); renderPreview(); });
    company.addEventListener('input', ()=>{ it.company=company.value; pushHistory(); persistState(true); renderPreview(); });
    period.addEventListener('input', ()=>{ it.period=period.value; pushHistory(); persistState(true); renderPreview(); });
    desc.addEventListener('input', ()=>{ it.description=desc.value; pushHistory(); persistState(true); renderPreview(); });
    const actions = el('div',{className:'item-actions'});
    const del = el('button',{className:'btn secondary'}, 'Remove');
    del.onclick = ()=>{ state.experience.splice(idx,1); pushHistory(); persistState(true); renderExp(); renderPreview(); };
    actions.appendChild(del);
    card.appendChild(role); card.appendChild(company); card.appendChild(period); card.appendChild(desc); card.appendChild(actions);
    els.expList.appendChild(card);
  });
}
function renderEdu(){
  els.eduList.innerHTML = '';
  state.education.forEach((it, idx)=>{
    const card = el('div',{className:'item-card'});
    const degree = el('input',{type:'text', placeholder:'Degree', value:it.degree || ''});
    const school = el('input',{type:'text', placeholder:'School/University', value:it.school || ''});
    const year = el('input',{type:'text', placeholder:'Year/Duration', value:it.year || ''});
    const desc = document.createElement('textarea'); desc.placeholder='Description/notes'; desc.value = it.description || '';
    [degree, school, year, desc].forEach(x=>{ x.style.width='100%'; x.style.marginBottom='8px'; });
    degree.addEventListener('input', ()=>{ it.degree=degree.value; pushHistory(); persistState(true); renderPreview(); });
    school.addEventListener('input', ()=>{ it.school=school.value; pushHistory(); persistState(true); renderPreview(); });
    year.addEventListener('input', ()=>{ it.year=year.value; pushHistory(); persistState(true); renderPreview(); });
    desc.addEventListener('input', ()=>{ it.description=desc.value; pushHistory(); persistState(true); renderPreview(); });
    const actions = el('div',{className:'item-actions'});
    const del = el('button',{className:'btn secondary'}, 'Remove');
    del.onclick = ()=>{ state.education.splice(idx,1); pushHistory(); persistState(true); renderEdu(); renderPreview(); };
    actions.appendChild(del);
    card.appendChild(degree); card.appendChild(school); card.appendChild(year); card.appendChild(desc); card.appendChild(actions);
    els.eduList.appendChild(card);
  });
}
function renderProjects(){
  els.projList.innerHTML = '';
  state.projects.forEach((it, idx)=>{
    const card = el('div',{className:'item-card'});
    const title = el('input',{type:'text', placeholder:'Project Title', value:it.title || ''});
    const link = el('input',{type:'text', placeholder:'Link (optional)', value:it.link || ''});
    const desc = document.createElement('textarea'); desc.placeholder='Description'; desc.value = it.description || '';
    [title, link, desc].forEach(x=>{ x.style.width='100%'; x.style.marginBottom='8px'; });
    title.addEventListener('input', ()=>{ it.title=title.value; pushHistory(); persistState(true); renderPreview(); });
    link.addEventListener('input', ()=>{ it.link=link.value; pushHistory(); persistState(true); renderPreview(); });
    desc.addEventListener('input', ()=>{ it.description=desc.value; pushHistory(); persistState(true); renderPreview(); });
    const actions = el('div',{className:'item-actions'});
    const del = el('button',{className:'btn secondary'}, 'Remove');
    del.onclick = ()=>{ state.projects.splice(idx,1); pushHistory(); persistState(true); renderProjects(); renderPreview(); };
    actions.appendChild(del);
    card.appendChild(title); card.appendChild(link); card.appendChild(desc); card.appendChild(actions);
    els.projList.appendChild(card);
  });
}
function renderLangs(){
  els.langList.innerHTML = '';
  state.languages.forEach((it, idx)=>{
    const card = el('div',{className:'item-card'});
    const name = el('input',{type:'text', placeholder:'Language', value:it.name || ''});
    const level = el('input',{type:'text', placeholder:'Level', value:it.level || ''});
    [name, level].forEach(x=>{ x.style.width='100%'; x.style.marginBottom='8px'; });
    name.addEventListener('input', ()=>{ it.name=name.value; pushHistory(); persistState(true); renderPreview(); });
    level.addEventListener('input', ()=>{ it.level=level.value; pushHistory(); persistState(true); renderPreview(); });
    const actions = el('div',{className:'item-actions'});
    const del = el('button',{className:'btn secondary'}, 'Remove');
    del.onclick = ()=>{ state.languages.splice(idx,1); pushHistory(); persistState(true); renderLangs(); renderPreview(); };
    actions.appendChild(del);
    card.appendChild(name); card.appendChild(level); card.appendChild(actions);
    els.langList.appendChild(card);
  });
}
function renderCerts(){
  els.certList.innerHTML = '';
  state.certs.forEach((it, idx)=>{
    const card = el('div',{className:'item-card'});
    const name = el('input',{type:'text', placeholder:'Certification', value:it || ''});
    name.style.width='100%'; name.style.marginBottom='8px';
    name.addEventListener('input', ()=>{ state.certs[idx]=name.value; pushHistory(); persistState(true); renderPreview(); });
    const actions = el('div',{className:'item-actions'});
    const del = el('button',{className:'btn secondary'}, 'Remove');
    del.onclick = ()=>{ state.certs.splice(idx,1); pushHistory(); persistState(true); renderCerts(); renderPreview(); };
    actions.appendChild(del);
    card.appendChild(name); card.appendChild(actions);
    els.certList.appendChild(card);
  });
}
function renderCustom(){
  els.customSections.innerHTML = '';
  state.custom.forEach((it, idx)=>{
    const card = el('div',{className:'item-card'});
    const title = el('input',{type:'text', placeholder:'Section title', value:it.title || ''});
    const list = document.createElement('div');
    (it.items||[]).forEach((itItem, i2)=>{
      const itemInput = el('input',{type:'text', placeholder:'Item', value:itItem});
      itemInput.style.width='100%'; itemInput.style.marginBottom='8px';
      itemInput.addEventListener('input', ()=>{ it.items[i2]=itemInput.value; pushHistory(); persistState(true); renderPreview(); });
      const delBtn = el('button',{className:'btn secondary'}, 'Remove');
      delBtn.onclick = ()=>{ it.items.splice(i2,1); pushHistory(); persistState(true); renderCustom(); renderPreview(); };
      const row = el('div',{}, itemInput);
      row.appendChild(delBtn);
      list.appendChild(row);
    });
    const addItemBtn = el('button',{className:'btn'}, 'Add item');
    addItemBtn.onclick = ()=>{ it.items = it.items || []; it.items.push(''); pushHistory(); persistState(true); renderCustom(); renderPreview(); };
    title.addEventListener('input', ()=>{ it.title = title.value; pushHistory(); persistState(true); renderPreview(); });
    const actions = el('div',{className:'item-actions'});
    const del = el('button',{className:'btn secondary'}, 'Remove Section');
    del.onclick = ()=>{ state.custom.splice(idx,1); pushHistory(); persistState(true); renderCustom(); renderPreview(); };
    actions.appendChild(del);
    card.appendChild(title); card.appendChild(list); card.appendChild(addItemBtn); card.appendChild(actions);
    els.customSections.appendChild(card);
  });
}

// wire up UI events to state
function attachEvents(){
  // personal fields
  ['fullName','email','phone','title','location','summary'].forEach(id=>{
    const elRef = els[id];
    elRef.addEventListener('input', ()=>{
      state.personal[id] = elRef.value;
      updateWordCount();
      pushHistory(); persistState(true); renderPreview();
    });
  });

  // social
  ['linkedin','github','portfolio','twitter'].forEach(k=>{
    const elRef = els[k];
    elRef.addEventListener('input', ()=>{
      state.social[k] = elRef.value;
      pushHistory(); persistState(true); renderPreview();
    });
  });

  // skills
  els.addSkillBtn.addEventListener('click', ()=>{
    const name = els.newSkill.value.trim();
    const level = +els.skillLevel.value || 60;
    if(!name) return;
    state.skills.push({name, level});
    els.newSkill.value = '';
    pushHistory(); persistState(true); renderSkills(); renderPreview();
  });

  // add experience/education/project
  els.addExperience.addEventListener('click', ()=>{
    state.experience.push({role:'', company:'', period:'', description:''});
    pushHistory(); persistState(true); renderExp(); renderPreview();
  });
  els.addEducation.addEventListener('click', ()=>{
    state.education.push({degree:'', school:'', year:'', description:''});
    pushHistory(); persistState(true); renderEdu(); renderPreview();
  });
  els.addProject.addEventListener('click', ()=>{
    state.projects.push({title:'', link:'', description:''});
    pushHistory(); persistState(true); renderProjects(); renderPreview();
  });

  // languages, certs, custom sections
  els.addLang.addEventListener('click', ()=>{
    const name = els.newLang.value.trim(); const level = els.langLevel.value;
    if(!name) return;
    state.languages.push({name, level});
    els.newLang.value='';
    pushHistory(); persistState(true); renderLangs(); renderPreview();
  });
  els.addCert.addEventListener('click', ()=>{
    const val = els.newCert.value.trim(); if(!val) return;
    state.certs.push(val); els.newCert.value='';
    pushHistory(); persistState(true); renderCerts(); renderPreview();
  });
  els.addCustomSection.addEventListener('click', ()=>{
    const title = els.newCustomTitle.value.trim() || 'Custom';
    state.custom.push({title, items:[]}); els.newCustomTitle.value='';
    pushHistory(); persistState(true); renderCustom(); renderPreview();
  });

  // photo upload
  els.photoUpload.addEventListener('change', (ev)=>{
    const f = ev.target.files && ev.target.files[0];
    if(!f) return;
    const reader = new FileReader();
    reader.onload = (e)=>{
      state.personal.avatarDataUrl = e.target.result;
      pushHistory(); persistState(true); renderPreview();
    };
    reader.readAsDataURL(f);
    ev.target.value = '';
  });
  els.clearPhoto.addEventListener('click', ()=>{
    state.personal.avatarDataUrl = null; pushHistory(); persistState(true); renderPreview();
  });

  // save & download PDF (user chose B)
  els.saveBtn.addEventListener('click', ()=>{ saveAndMaybeDownloadPdf(true); });

  // download PDF explicit button
  els.downloadPdf.addEventListener('click', ()=>{ exportPdf(); });

  // export JSON
  els.exportJsonBtn.addEventListener('click', ()=>{
    const blob = new Blob([JSON.stringify(state, null, 2)], {type:'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = `${(state.personal.fullName||'resume').replace(/\s+/g,'_')}_data.json`;
    a.click();
    URL.revokeObjectURL(url);
    showToast('Exported JSON ✓');
  });

  // import JSON
  els.importBtn.addEventListener('click', ()=> els.importJsonFile.click());
  els.importJsonFile.addEventListener('change', (ev)=>{
    const f = ev.target.files && ev.target.files[0];
    if(!f) return;
    const reader = new FileReader();
    reader.onload = (e)=>{
      try{
        const data = JSON.parse(e.target.result);
        state = Object.assign(deepClone(defaultState), data);
        pushHistory(); persistState(false); renderAll(); showToast('Imported ✓');
      }catch(err){
        alert('Invalid JSON file');
      }
    };
    reader.readAsText(f);
    ev.target.value='';
  });

  // download .doc
  els.downloadDoc.addEventListener('click', ()=>{
    const docHtml = document.getElementById('previewInner').outerHTML;
    const blob = new Blob(['\ufeff', docHtml], {type:'application/msword'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = `${(state.personal.fullName||'resume').replace(/\s+/g,'_')}.doc`;
    a.click();
    URL.revokeObjectURL(url);
    showToast('DOC downloaded ✓');
  });

  // theme toggle
  els.toggleTheme.addEventListener('click', ()=>{
    if(document.body.classList.contains('dark')) { document.body.classList.remove('dark'); state.theme='light'; localStorage.setItem('theme','light'); }
    else { document.body.classList.add('dark'); state.theme='dark'; localStorage.setItem('theme','dark'); }
    pushHistory(); persistState(true);
  });

  // undo/redo
  els.undoBtn.addEventListener('click', undo);
  els.redoBtn.addEventListener('click', redo);

  // reset
  els.resetBtn.addEventListener('click', ()=>{
    if(!confirm('Reset resume to default content? This will overwrite current data.')) return;
    state = deepClone(defaultState);
    pushHistory(); persistState(false); renderAll(); showToast('Reset ✓');
  });

  // template modal
  els.templateBtn.addEventListener('click', ()=> els.templateModal.style.display='flex');
  els.closeTemplate.addEventListener('click', ()=> els.templateModal.style.display='none');
  els.templateModal.addEventListener('click', (ev)=>{ if(ev.target===els.templateModal) els.templateModal.style.display='none'; });
  els.templateGrid.addEventListener('click', (ev)=>{
    const card = ev.target.closest('.template-card');
    if(!card) return;
    document.querySelectorAll('.template-card').forEach(c=>c.classList.remove('active'));
    card.classList.add('active');
    state.template = card.dataset.template;
    document.body.classList.remove('template-minimal','template-classic');
    if(state.template==='minimal') document.body.classList.add('template-minimal');
    if(state.template==='classic') document.body.classList.add('template-classic');
    pushHistory(); persistState(true); renderPreview();
  });

  // keyboard shortcuts
  window.addEventListener('keydown', (ev)=>{
    if((ev.ctrlKey||ev.metaKey) && ev.key.toLowerCase() === 's'){
      ev.preventDefault();
      saveAndMaybeDownloadPdf(true);
    }
    if((ev.ctrlKey||ev.metaKey) && ev.key.toLowerCase() === 'p'){
      ev.preventDefault();
      exportPdf();
    }
    if((ev.ctrlKey||ev.metaKey) && ev.key.toLowerCase() === 'z'){ ev.preventDefault(); undo(); }
    if((ev.ctrlKey||ev.metaKey) && (ev.key.toLowerCase() === 'y' || (ev.shiftKey && ev.key.toLowerCase()==='z'))){ ev.preventDefault(); redo(); }
  });
}

// word count
function updateWordCount(){
  const words = (els.summary.value || '').trim().split(/\s+/).filter(Boolean).length;
  els.wordCount.textContent = `Words: ${words}`;
}

// Save and optionally auto-download PDF (user chose auto-download on Save)
function saveAndMaybeDownloadPdf(shouldDownloadPdf){
  pushHistory();
  persistState(false);
  showToast('Saved ✓');
  if(shouldDownloadPdf){
    // small delay to ensure preview updated/painted
    setTimeout(()=>{ exportPdf(); }, 300);
  }
}

// Export PDF using html2pdf
function exportPdf(){
  const element = document.getElementById('previewInner');
  // set options for html2pdf
  const opt = {
    margin: 0.5,
    filename: `${(state.personal.fullName||'resume').replace(/\s+/g,'_')}.pdf`,
    image: { type: 'jpeg', quality: 0.98 },
    html2canvas: { scale: 2, useCORS:true },
    jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
  };
  // temporarily remove focus outlines for better print
  document.activeElement && document.activeElement.blur();
  html2pdf().set(opt).from(element).save().then(()=>{ showToast('PDF downloaded ✓'); });
}

// initial load
function init(){
  loadState();
  pushHistory(); // initial state in history
  renderAll();
  attachEvents();
  updateUndoRedoButtons();
}

init();
</script>
</body>
</html>
