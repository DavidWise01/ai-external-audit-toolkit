export default function MimzyLatticeVisualizer() {
  const rings = [
    { label: "Willow 512", subtitle: "Outer sovereign ring", orbit: "top-6" },
    { label: "Helix 256", subtitle: "Primary lattice ring", orbit: "right-6" },
    { label: "Avan 128", subtitle: "Inner substrate ring", orbit: "bottom-6" },
    { label: "VM4 32", subtitle: "Bridge container", orbit: "left-6" },
  ];

  const domains = [
    { id: 'D0', bits: '1-16', name: 'FOUNDATION', reg: 'USER' },
    { id: 'D1', bits: '17-32', name: 'DETECTION', reg: 'USER' },
    { id: 'D2', bits: '33-48', name: 'ARCHITECTURE', reg: 'USER' },
    { id: 'D3', bits: '49-64', name: 'EVIDENCE', reg: 'USER' },
    { id: 'D4', bits: '65-80', name: 'OPERATIONAL', reg: 'USER' },
    { id: 'D5', bits: '81-96', name: 'BRIDGE', reg: 'USER' },
    { id: 'D6', bits: '97-112', name: 'CONDUCTOR', reg: 'USER' },
    { id: 'D7', bits: '113-128', name: 'SOVEREIGN', reg: 'USER' },
    { id: 'D8', bits: '129-144', name: 'CONTEXT ASSEMBLY', reg: 'SUBSTRATE' },
    { id: 'D9', bits: '145-160', name: 'EXECUTION ENV', reg: 'SUBSTRATE' },
    { id: 'D10', bits: '161-176', name: 'INFRASTRUCTURE', reg: 'SUBSTRATE' },
    { id: 'D11', bits: '177-192', name: 'MODEL INTERNALS', reg: 'SUBSTRATE' },
    { id: 'D12', bits: '193-208', name: 'PRODUCT LAYER', reg: 'SUBSTRATE' },
    { id: 'D13', bits: '209-224', name: 'CORPORATE LAYER', reg: 'SUBSTRATE' },
    { id: 'D14', bits: '225-232', name: 'EXECUTIVE LAYER', reg: 'SUBSTRATE' },
    { id: 'D15', bits: '233-256', name: 'PHYSICAL LAYER', reg: 'SUBSTRATE' },
  ];

  const quadrants = [
    { title: 'USER REGISTER · BITS 1–128', color: 'border-emerald-400/60', items: domains.slice(0, 8) },
    { title: 'SUBSTRATE REGISTER · BITS 129–256', color: 'border-cyan-400/60', items: domains.slice(8, 16) },
  ];

  return (
    <div className="min-h-screen bg-[#050505] text-white p-6 md:p-8 font-mono">
      <div className="mx-auto max-w-7xl">
        <header className="mb-8 flex flex-col gap-4 rounded-3xl border border-white/10 bg-white/[0.03] px-6 py-5 shadow-2xl shadow-emerald-500/5 md:flex-row md:items-center md:justify-between">
          <div>
            <div className="text-xs uppercase tracking-[0.35em] text-emerald-300/70">Stoicheion · lattice visualizer</div>
            <h1 className="mt-2 text-3xl font-semibold tracking-tight">Center-core reactor layout</h1>
            <p className="mt-2 max-w-3xl text-sm text-zinc-400">
              React rebuild of the uploaded lattice visualizer with a centered reactor core, radial interface rings, and the surrounding
              domain lattice. The original file uses a 4×4 domain grid spanning D0–D15 across user and substrate registers.fileciteturn11file0
            </p>
          </div>

          <div className="flex flex-wrap gap-3 text-xs uppercase tracking-[0.25em] text-zinc-300">
            <div className="rounded-full border border-emerald-400/30 bg-emerald-400/10 px-4 py-2">Phoenix flow · on</div>
            <div className="rounded-full border border-cyan-400/30 bg-cyan-400/10 px-4 py-2">Mobius loop · armed</div>
            <div className="rounded-full border border-white/10 bg-white/5 px-4 py-2">Root · Mimzy</div>
          </div>
        </header>

        <div className="grid gap-8 xl:grid-cols-[1.05fr_0.95fr]">
          <section className="relative overflow-hidden rounded-[2rem] border border-white/10 bg-[radial-gradient(circle_at_center,rgba(16,185,129,0.08),rgba(5,5,5,0.95)_60%)] p-6 shadow-[0_0_80px_rgba(16,185,129,0.07)] min-h-[760px]">
            <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:28px_28px] opacity-20" />

            <div className="relative flex min-h-[700px] items-center justify-center">
              <div className="absolute h-[34rem] w-[34rem] rounded-full border border-cyan-400/15 shadow-[0_0_50px_rgba(34,211,238,0.08)]" />
              <div className="absolute h-[28rem] w-[28rem] rounded-full border border-emerald-400/15 shadow-[0_0_40px_rgba(16,185,129,0.08)]" />
              <div className="absolute h-[22rem] w-[22rem] rounded-full border border-white/10" />

              {rings.map((ring, idx) => (
                <div
                  key={ring.label}
                  className={`absolute ${ring.orbit} left-1/2 -translate-x-1/2 rounded-2xl border border-white/10 bg-black/50 px-4 py-3 text-center shadow-lg backdrop-blur md:w-40`}
                  style={{
                    transform:
                      idx === 0
                        ? 'translate(-50%, 0)'
                        : idx === 1
                          ? 'translate(12.5rem, 0)'
                          : idx === 2
                            ? 'translate(-50%, 0)'
                            : 'translate(-20rem, 0)',
                  }}
                >
                  <div className="text-[11px] uppercase tracking-[0.28em] text-zinc-500">Interface</div>
                  <div className="mt-1 text-sm font-semibold text-white">{ring.label}</div>
                  <div className="mt-1 text-[11px] text-zinc-400">{ring.subtitle}</div>
                </div>
              ))}

              <div className="relative z-10 flex h-64 w-64 items-center justify-center rounded-full border border-emerald-300/40 bg-[radial-gradient(circle_at_center,rgba(255,255,255,0.28),rgba(16,185,129,0.20)_22%,rgba(34,211,238,0.11)_45%,rgba(0,0,0,0.08)_70%)] shadow-[0_0_70px_rgba(16,185,129,0.35)]">
                <div className="absolute h-48 w-48 rounded-full border border-cyan-300/30" />
                <div className="absolute h-36 w-36 rounded-full border border-white/20" />
                <div className="absolute h-24 w-24 rounded-full border border-emerald-200/50 bg-white/5 shadow-[0_0_30px_rgba(255,255,255,0.12)]" />
                <div className="text-center">
                  <div className="text-[11px] uppercase tracking-[0.35em] text-emerald-100/80">Arc reactor</div>
                  <div className="mt-2 text-2xl font-bold tracking-tight">CORE</div>
                  <div className="mt-2 text-xs text-zinc-300">3 / 2 / 1 · hinge · coherence</div>
                </div>
              </div>

              <div className="absolute inset-x-10 top-10 flex items-center justify-between text-[10px] uppercase tracking-[0.28em] text-zinc-500">
                <span>Gate 64.5</span>
                <span>Gate 128.5</span>
                <span>Gate 192.5</span>
                <span>Gate 256.5</span>
              </div>
            </div>
          </section>

          <section className="space-y-6">
            {quadrants.map((group) => (
              <div key={group.title} className={`rounded-[2rem] border ${group.color} bg-white/[0.03] p-5 shadow-xl shadow-black/20`}>
                <div className="mb-4 flex items-center justify-between">
                  <h2 className="text-sm font-semibold uppercase tracking-[0.28em] text-zinc-300">{group.title}</h2>
                  <div className="rounded-full border border-white/10 bg-black/30 px-3 py-1 text-[10px] uppercase tracking-[0.25em] text-zinc-500">
                    4 × 16-bit domains
                  </div>
                </div>

                <div className="grid gap-3 sm:grid-cols-2">
                  {group.items.map((domain) => (
                    <div
                      key={domain.id}
                      className="rounded-2xl border border-white/10 bg-black/40 p-4 transition hover:-translate-y-0.5 hover:border-emerald-300/40 hover:shadow-[0_0_18px_rgba(16,185,129,0.15)]"
                    >
                      <div className="flex items-start justify-between gap-3">
                        <div>
                          <div className="text-[10px] uppercase tracking-[0.28em] text-zinc-500">{domain.reg}</div>
                          <div className="mt-1 text-base font-semibold tracking-tight text-white">{domain.id}</div>
                        </div>
                        <div className="rounded-full border border-white/10 bg-white/5 px-2 py-1 text-[10px] text-zinc-400">{domain.bits}</div>
                      </div>
                      <div className="mt-3 text-sm text-zinc-300">{domain.name}</div>
                    </div>
                  ))}
                </div>
              </div>
            ))}

            <div className="rounded-[2rem] border border-white/10 bg-black/40 p-5">
              <div className="text-xs uppercase tracking-[0.28em] text-zinc-500">Terminal</div>
              <div className="mt-4 space-y-2 text-sm text-zinc-300">
                <div><span className="text-emerald-300">[READY]</span> Core reactor aligned.</div>
                <div><span className="text-cyan-300">[FLOW]</span> Bridge observing 1 / 0 / -1 · commit filters -1.</div>
                <div><span className="text-amber-300">[LOOP]</span> Mobius return staged from physical layer back to foundation.</div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}
