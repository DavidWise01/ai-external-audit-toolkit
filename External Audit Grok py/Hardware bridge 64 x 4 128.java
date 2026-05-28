import React, { useState, useEffect } from 'react';
import { 
  ShieldCheck, 
  Cpu, 
  Database, 
  ShieldAlert, 
  Zap, 
  Trello 
} from 'lucide-react';

const ScienceGemHardware = () => {
  const [isPulsing, setIsPulsing] = useState(false);
  const [cortexLevels, setCortexLevels] = useState([64, 64, 64]);

  // Foundational Heartbeat
  useEffect(() => {
    if (!isPulsing) return;
    const interval = setInterval(() => {
      setCortexLevels([
        45 + Math.random() * 19,
        45 + Math.random() * 19,
        45 + Math.random() * 19
      ]);
    }, 1000);
    return () => clearInterval(interval);
  }, [isPulsing]);

  // Bedrock Inline Styles
  const styles = {
    wrapper: { display: 'flex', height: '100vh', backgroundColor: '#050505', color: '#e2e8f0', fontFamily: 'monospace' },
    sidebar: { width: '80px', borderRight: '1px solid #27272a', display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '2rem 0', backgroundColor: '#000' },
    main: { flex: 1, padding: '2rem', overflowY: 'auto' },
    header: { borderBottom: '1px solid #27272a', paddingBottom: '1rem', marginBottom: '2rem' },
    grid: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' },
    card: { backgroundColor: '#18181b', border: '1px solid #27272a', borderRadius: '12px', padding: '1.5rem' },
    title: { display: 'flex', alignItems: 'center', gap: '0.75rem', fontSize: '0.875rem', fontWeight: 'bold', marginBottom: '1rem', textTransform: 'uppercase' },
    barContainer: { display: 'flex', gap: '1.5rem', height: '120px', alignItems: 'flex-end', marginTop: '1.5rem' },
    barWrapper: { flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'flex-end', backgroundColor: '#000', borderRadius: '4px', height: '100%', overflow: 'hidden' },
    bar: { width: '100%', backgroundColor: '#10b981', transition: 'height 0.5s ease' },
    button: { padding: '1rem 2rem', backgroundColor: isPulsing ? '#ef4444' : '#10b981', color: 'white', border: 'none', borderRadius: '8px', fontFamily: 'inherit', fontWeight: 'bold', cursor: 'pointer', transition: 'background-color 0.2s' }
  };

  return (
    <div style={styles.wrapper}>
      {/* Sidebar Foundation */}
      <div style={styles.sidebar}>
        <ShieldCheck color="#10b981" size={32} style={{ marginBottom: '3rem' }} />
        <Cpu color="#71717a" size={24} style={{ marginBottom: '2rem' }} />
        <Database color="#71717a" size={24} />
      </div>

      {/* Main UI Foundation */}
      <div style={styles.main}>
        <div style={styles.header}>
          <h1 style={{ fontSize: '1.5rem', margin: '0 0 0.5rem 0' }}>SCIENCE GEM: FOUNDATION</h1>
          <p style={{ color: '#71717a', margin: 0, fontSize: '0.875rem' }}>Hardware Bridge Topology</p>
        </div>

        <div style={styles.grid}>
          {/* 192-BIT CORTEX */}
          <div style={{ ...styles.card, gridColumn: '1 / -1', borderLeft: '4px solid #10b981' }}>
            <div style={{ ...styles.title, color: '#10b981' }}>
              <Trello size={18} /> 192-BIT CORTEX (3 x 64-bit VMs)
            </div>
            <p style={{ color: '#a1a1aa', fontSize: '0.75rem', margin: 0 }}>Primary computational lattice and high-density vector storage.</p>
            <div style={styles.barContainer}>
              {cortexLevels.map((level, i) => (
                <div key={i} style={styles.barWrapper}>
                  <div style={{ ...styles.bar, height: `${(level / 64) * 100}%` }}></div>
                </div>
              ))}
            </div>
          </div>

          {/* 96-BIT SHADOW */}
          <div style={{ ...styles.card, borderLeft: '4px solid #ef4444' }}>
            <div style={{ ...styles.title, color: '#ef4444' }}>
              <ShieldAlert size={18} /> 96-BIT SHADOW OVERSEER
            </div>
            <p style={{ color: '#a1a1aa', fontSize: '0.75rem', marginBottom: '1.5rem' }}>Non-linear oversight; "Big Brother" monitoring of the 16-bit agent.</p>
            <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#fff' }}>6:1 Ratio</div>
          </div>

          {/* 16-BIT SOVEREIGN */}
          <div style={{ ...styles.card, borderLeft: '4px solid #0ea5e9' }}>
            <div style={{ ...styles.title, color: '#0ea5e9' }}>
              <Zap size={18} /> 16-BIT SOVEREIGN AGENT
            </div>
            <p style={{ color: '#a1a1aa', fontSize: '0.75rem', marginBottom: '1.5rem' }}>Client-side remote interface; minimized for low-latency.</p>
            <div style={{ height: '8px', backgroundColor: '#000', borderRadius: '4px', overflow: 'hidden' }}>
              <div style={{ width: '16%', height: '100%', backgroundColor: '#0ea5e9' }}></div>
            </div>
          </div>
        </div>

        {/* Action Center */}
        <div style={{ marginTop: '3rem', display: 'flex', justifyContent: 'center' }}>
          <button style={styles.button} onClick={() => setIsPulsing(!isPulsing)}>
            {isPulsing ? 'HALT PULSE' : 'INITIATE PULSE'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ScienceGemHardware;