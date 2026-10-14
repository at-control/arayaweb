"""Company content for the homepage and service pages.

Sources: the owner's live website (services, project-scope, clients, about and team pages)
and owner-supplied project scopes. See docs/CONTENT-SOURCES.md.
"""

CLIENTS = [
    {'name': 'PT PELNI (Persero)', 'logo': 'client-pelni.webp', 'width': 526, 'height': 160},
    {'name': 'Pertamina', 'logo': 'client-pertamina.svg', 'width': 1097, 'height': 255},
    {'name': 'Pelindo', 'logo': 'client-pelindo.webp', 'width': 774, 'height': 160},
    {'name': 'TNI Angkatan Laut (Indonesian Navy)', 'logo': 'client-tni-al.webp', 'width': 141, 'height': 160, 'emblem': True},
    {'name': 'PT Samudera Indonesia Tbk', 'logo': 'client-samudera-indonesia.webp', 'width': 1040, 'height': 160},
    {'name': 'PT USDA Seroja Jaya shipyard', 'logo': 'client-usda-seroja-jaya.webp', 'width': 588, 'height': 144},
    {'name': 'PT Armada Cakrawala Esa', 'logo': 'client-armada-cakrawala-esa.webp', 'width': 179, 'height': 53},
]

# Names and roles from the owner's reference; portraits from the original site.
LEADERSHIP = [
    {'name': 'Arif Fatkur Rohman, S.T., M.MT.', 'role': 'Director', 'image': 'leadership-arif', 'height': 870},
    {'name': 'M Rosul Akbar', 'role': 'Manager', 'image': 'leadership-rosul', 'height': 708},
    {'name': 'Anjas Budiarso', 'role': 'Manager', 'image': 'leadership-anjas', 'height': 960},
]

# Work gallery paused at the owner's request; keep these photos for later reuse.
# Owner-provided photos, 14 October 2026. Captions describe the visible work;
# project/vessel names and exact job scope have not been supplied.
WORK_PHOTOS = [
    {'stem': 'work-engine-room', 'width': 1280, 'height': 596,
     'title': 'Marine machinery', 'caption': 'Engineering work in the engine room.',
     'alt': 'Araya personnel working around machinery in a vessel’s engine room'},
    {'stem': 'work-switchboard', 'width': 1280, 'height': 960,
     'title': 'Electrical systems', 'caption': 'Onboard switchboard inspection and technical review.',
     'alt': 'Araya personnel reviewing an onboard electrical switchboard'},
]

# label, service page, anchor on that page
CAPABILITIES = [
    ('Fire alarm & monitoring', 'marine', 'alarms'),
    ('Engine safety devices', 'marine', 'safety'),
    ('Generator systems', 'marine', 'generators'),
    ('Manoeuvring, CPP & bow thrusters', 'marine', 'propulsion'),
    ('Deck cranes', 'marine', 'cranes'),
    ('CNC & wire-cut machines', 'industrial', 'machinery'),
    ('Industrial cranes', 'industrial', 'cranes'),
    ('MV/LV generators', 'industrial', 'generators'),
    ('PLC, HMI & SCADA', 'automation', 'plc'),
    ('Switchboards & MCC', 'automation', 'panels'),
    ('Hazardous-area equipment', 'automation', 'hazardous'),
    ('Electronic card repair', 'automation', 'electronics'),
]

BRAND_GROUPS = [
    ('Automation & control', ['Siemens', 'ABB', 'Schneider Electric', 'Omron', 'Mitsubishi', 'Allen-Bradley', 'Honeywell', 'Modicon']),
    ('Marine systems', ['Consilium', 'Autronica', 'Tyco', 'MEDC', 'SIMOS', 'MaK', 'Janssen', 'Stein Sohn']),
    ('Power generation', ['Stamford', 'Leroy-Somer', 'Marathon', 'Caterpillar', 'SDMO', 'Denyo', 'GE']),
    ('Hazardous area', ['Stahl', 'Chalmit', 'Crouse-Hinds', 'CEAG', 'Glamox', 'Orga']),
    ('Machine tools', ['Fanuc', 'Okuma', 'Makino', 'Mori Seiki', 'Toshiba', 'Charmilles']),
]

SERVICES = {
    'marine': {
        'name': 'Marine', 'short': 'marine', 'label': 'Marine engineering',
        'title': 'Marine Electrical & Automation Services Indonesia | Araya',
        'description': 'Marine engineering in Indonesia: fire alarm and AMS, engine overhaul and control, generator synchronisation, steering, cargo monitoring and system retrofit.',
        'heading': 'Marine engineering.<br>Engine room to bridge.',
        'intro': 'Supply and repair of electrical, mechanical and automation systems on board.',
        'hero_image': 'marine.webp', 'hero_width': 767, 'hero_height': 883, 'hero_alt': 'Araya technician inspecting marine engine equipment',
        'card_image': 'marine.webp', 'card_width': 767, 'card_height': 883, 'card_alt': 'Technical inspection of marine engine equipment',
        'summary': 'Supply and repair of onboard systems, from engine room to bridge.',
        'highlights': ['Fire alarm, general alarm & monitoring', 'Engine safety devices', 'Manoeuvring, CPP & bow thrusters', 'Deck cranes, AC & refrigeration'],
        'scope_heading': 'Systems we repair,<br>upgrade and retrofit.',
        'overview': 'We supply and repair onboard systems, and modify, upgrade or retrofit obsolete and end-of-sale equipment so it can stay in service.',
        'groups': [
            ('alarms', 'Fire alarm, general alarm & AMS', 'Supply, repair and retrofit of ship fire-alarm, general-alarm and alarm monitoring systems (AMS), including associated fire-door equipment. Work covers monitoring signals, alarm indication and interfaces between onboard systems, according to the vessel’s existing installation.'),
            ('safety', 'Engine safety devices', 'Engine safety devices and alarms for main and auxiliary engines, including Sinpol-D systems. We assess the existing sensors, alarm signals and shutdown interfaces when repairing or replacing equipment, so the work is defined around the engine’s protection requirements.'),
            ('engines', 'Engine overhaul, control & monitoring', 'Overhaul and repair of auxiliary and emergency diesel engines, together with propulsion-engine control, throttle and monitoring work. Mechanical and control requirements are assessed together so replacements, repairs or modifications fit the existing engine installation.'),
            ('generators', 'Generator control & synchronisation', 'Ship generator and emergency-generator supply and repair, including automatic start/stop, generator synchronisation and load sharing. Single-generator and parallel-generator systems have different control requirements; the scope considers the existing engine, governor, AVR, breakers and power-management arrangement.'),
            ('propulsion', 'Steering, manoeuvring, CPP & bow thrusters', 'Repair and retrofit of steering and manoeuvring controls, controllable-pitch propeller (CPP) systems and bow-thruster controls. We review command, feedback and control interfaces across the existing installation to define replacement or modification work.'),
            ('navigation', 'Navigation & public address', 'Service and repair of navigation equipment, including autopilot and gyro-compass systems, together with onboard public-address systems. The work considers the equipment model, existing connections and interfaces with other bridge systems when planning repair or replacement.'),
            ('automation', 'Electrical panels, PLC & SCADA', 'Repair and retrofit of onboard electrical installations, control panels, PLC, HMI and SCADA systems. We review the existing control functions, field signals and operator displays when defining software changes, panel modifications or replacement of obsolete equipment.'),
            ('water-level', 'Water-level monitoring', 'Water-level monitoring for tanks, bilges and other onboard measurement points. Work includes sensor replacement and integration with alarms or operator displays, selected around the measured liquid, mounting arrangement and existing signal interfaces.'),
            ('cargo-monitoring', 'Cargo monitoring systems', 'Cargo-monitoring systems, sensor signals and operator displays for vessel operations. We review the existing installation and its measurement points to define monitoring, equipment replacement or retrofit work suited to the cargo system and its operating requirements.'),
            ('cranes', 'Deck cranes & deck machinery', 'Supply and repair of deck cranes and deck machinery, including their electrical and control equipment. Fault assessment considers the machinery, operating controls and existing interlocks, with repair or modification scope defined around the installed system.'),
            ('hvac', 'AC & refrigeration systems', 'Supply and repair of onboard air-conditioning and refrigeration systems. We assess the installed equipment, electrical controls and reported operating problems to define the work, including replacement of suitable components or repair of the existing installation.'),
            ('retrofit', 'Retrofit of obsolete systems', 'Modification, upgrade and retrofit of obsolete or end-of-sale marine equipment. We review the functions that need to remain, existing signals and interfaces, and suitable replacements so the project can extend the useful life of the installed system.'),
        ],
        'equipment': [
            ('Fire & alarm systems', ['Consilium', 'Autronica', 'Siemens', 'Tyco', 'Honeywell', 'MEDC', 'Hekatron']),
            ('Manoeuvring & propulsion', ['SIMOS', 'CAMOS', 'Stein Sohn', 'MaK', 'Janssen']),
            ('Monitoring & engine control', ['Noris', 'ComAp', 'Sinpol-D']),
            ('Generators', ['Stamford', 'Leroy-Somer', 'ABB', 'Marathon', 'GE']),
        ],
        'featured': [('noris', 'Speed, temperature and pressure sensors, indicators, noriMos AMS, noriStar propulsion control and noriNet remote monitoring.'),
                     ('comap', 'Marine engine controllers, generator synchronisation, load sharing and vessel power management.')],
        'enquiry': ['Vessel name, type and current location', 'Equipment make, model and nameplate photo', 'Fault symptoms, alarm messages or the change you need', 'Wiring diagrams or system drawings, if available', 'Planned docking or maintenance window'],
    },
    'industrial': {
        'name': 'Industrial', 'short': 'industrial', 'label': 'Industrial engineering',
        'title': 'Industrial Machinery, Crane & Generator Services | Araya',
        'description': 'Supply and repair of CNC, wire-cut and EDM machines, overhead and portal cranes, MV/LV generators and production machinery across Indonesia.',
        'heading': 'Industrial machinery.<br>Back in production.',
        'intro': 'Supply and repair of industrial machines, cranes and MV/LV generators.',
        'hero_image': 'industrial.webp', 'hero_width': 767, 'hero_height': 883, 'hero_alt': 'Araya engineer working inside an industrial electrical cabinet',
        'card_image': 'industrial.webp', 'card_width': 767, 'card_height': 883, 'card_alt': 'Industrial electrical installation from Araya’s service photography',
        'summary': 'Supply and repair of production machinery, cranes and power equipment.',
        'highlights': ['CNC, wire-cut & EDM machines', 'Overhead, portal & luffing cranes', 'MV/LV generators', 'Casting, moulding & cutting machines'],
        'scope_heading': 'Machines and equipment<br>we supply and repair.',
        'overview': 'We supply and repair industrial machines and cranes, together with the electrical and control equipment that runs them.',
        'groups': [
            ('machinery', 'CNC lathes & milling machines', 'Supply and repair of CNC lathes and CNC milling machines used in industrial production. We assess machine faults together with the existing electrical and control systems to define repairs, component replacement or modifications appropriate to the installed machine.'),
            ('wirecut', 'Wire-cut & EDM machines', 'Supply and repair of wire-cut and electrical discharge machining (EDM) equipment. Work is defined around the machine model, reported faults and existing controls, with attention to the electrical equipment and interfaces involved in the machining process.'),
            ('cutting', 'NC gas & plasma cutting', 'Service and repair of NC gas-cutting and plasma-cutting machines, including PAC 500/600 equipment. We review the machine controls, electrical installation and fault symptoms to establish repair or replacement requirements for the existing cutting system.'),
            ('production', 'Hobbing, casting & moulding', 'Supply and repair of hobbing machines, continuous-casting equipment and moulding machines. Mechanical, electrical and automation requirements are considered in the context of the production equipment, with the scope based on its operating functions and existing controls.'),
            ('cranes', 'Crane supply & repair', 'Supply and repair of level-luffing, slewing, overhead, portal and port cranes, including P&H equipment. We review the installed machinery, electrical equipment and control functions when defining fault repair, replacement or a system upgrade.'),
            ('generators', 'MV/LV generators', 'Supply and repair of medium- and low-voltage industrial generators. The scope considers the generator rating, electrical connections, controls and operating arrangement, including the interfaces with the site’s existing power-distribution and generation systems.'),
            ('electrical', 'Panels & motor controls', 'Repair and modification of industrial electrical panels, MV/LV switchboards and motor-control centres. Work can include soft starters and variable-frequency drives, with selection and interfaces assessed around the connected motors, loads and existing control arrangement.'),
            ('automation', 'PLC, HMI & instrumentation', 'PLC, SCADA and HMI software work for industrial machines and process equipment, together with process instrumentation. We review operating sequences, field signals and operator displays when defining control changes or replacement of existing automation equipment.'),
        ],
        'equipment': [
            ('CNC & machine tools', ['Fanuc', 'Mitsubishi', 'Toshiba', 'Mori Seiki', 'Okuma', 'Makino']),
            ('Wire-cut & EDM', ['Charmilles', 'Fuji Electric', 'Fanuc']),
            ('Casting & cranes', ['CEIA', 'P&H']),
            ('Generators', ['GE', 'Leroy-Somer', 'Stamford', 'ABB', 'Marathon']),
        ],
        'featured': [('comap', 'Standby, prime-power and parallel generator control, load sharing and remote monitoring for industrial sites.'),
                     ('noris', 'Speed, temperature and pressure measurement, indicators and signal processing for machinery.')],
        'enquiry': ['Site name and location', 'Machine or generator make, model and nameplate photo', 'Fault symptoms, error codes or the upgrade you need', 'Electrical drawings and PLC/HMI project files, if available', 'Required completion date or shutdown window'],
    },
    'automation': {
        'name': 'Automation & Electrical', 'short': 'automation', 'label': 'Automation & electrical',
        'title': 'PLC, SCADA & Electrical Panel Services Indonesia | Araya',
        'description': 'PLC and SCADA software, switchboards and MCC, VFDs, hazardous-area equipment, protection relays and electronic card repair across Indonesia.',
        'heading': 'Automation &amp; electrical.<br>Control you can rely on.',
        'intro': 'PLC and SCADA, electrical power equipment, process instrumentation and electronic card repair.',
        'hero_image': 'control-room-1400.webp', 'hero_width': 1400, 'hero_height': 784, 'hero_variants': (('control-room-800.webp', 800), ('control-room-1400.webp', 1400)),
        'hero_alt': 'Marine control console with alarm panels and a Noris monitoring display',
        'card_image': 'control-room-1400.webp', 'card_width': 1400, 'card_height': 784, 'card_variants': (('control-room-800.webp', 800), ('control-room-1400.webp', 1400)),
        'card_alt': 'Marine control console with a Noris monitoring display',
        'summary': 'Control, power distribution and instrumentation for plants and vessels.',
        'highlights': ['PLC, HMI & SCADA', 'Switchboards, MCC & drives', 'Hazardous-area equipment', 'Protection relays & electronic cards'],
        'scope_heading': 'Control, power<br>and instrumentation.',
        'overview': 'We supply and repair the control, electrical power and instrumentation equipment that plants and vessels depend on.',
        'groups': [
            ('plc', 'PLC programming & retrofit', 'PLC hardware, programming and software modification for marine and industrial automation. Work includes replacement of obsolete or end-of-sale controllers, with existing sequences, input/output signals and connected equipment reviewed before defining the replacement and integration scope.'),
            ('scada', 'SCADA & HMI software', 'SCADA and HMI software for plant and onboard monitoring, alarms and operator control. We review the required displays, equipment signals and communication interfaces to define software changes or integration with the existing automation system.'),
            ('instrumentation', 'Process control & instrumentation', 'Automation and instrumentation for measuring and controlling process conditions. The work considers the sensors, signal interfaces and control functions already installed, together with the measurement and monitoring requirements of the plant or vessel.'),
            ('panels', 'Panels, switchboards & MCC', 'Supply, repair and modification of electrical panels, MV/LV switchboards and motor-control centres, with power and instrument cable supply. The scope considers connected equipment, control interfaces and the existing distribution arrangement for marine or industrial use.'),
            ('drives', 'Soft starters & VFDs', 'Supply and service of soft starters and variable-frequency drives (VFDs) for motor-control applications. Replacement and integration depend on the motor rating, load, required operating sequence and interfaces with existing panels or automation systems.'),
            ('motors', 'Electric motors', 'Supply and service of industrial and hazardous-area electric motors. Equipment selection and repair scope are based on the installed motor, electrical ratings, driven machinery and the site’s operating and installation requirements.'),
            ('hazardous', 'Hazardous-area apparatus', 'Supply and repair of electrical apparatus used in hazardous areas. Equipment selection and replacement must account for the site’s specified area classification, equipment certification, electrical ratings and installation requirements.'),
            ('protection', 'Electrical protection', 'Electrical protection equipment including circuit breakers, fuses, thermal-overload and earth-leakage relays, and Sepam or MiCOM protection relays. Repair and replacement requirements are assessed against the existing equipment, circuit arrangement and protection interfaces.'),
            ('power', 'Transformers, UPS & chargers', 'Supply and service of transformers, uninterruptible power supplies (UPS) and battery chargers for industrial and marine systems. The scope considers electrical ratings, connected loads and the existing power or battery arrangement when defining replacement or repair work.'),
            ('earthing', 'Surge protection, earthing & PFC', 'Lightning and surge protection, earthing equipment and reactive-power compensation, including power-factor correction (PFC). Work is defined around the installation’s existing equipment and electrical arrangement, including grounding or retractable grounding assemblies where applicable.'),
            ('gensets', 'Generators & generating sets', 'MV/LV generators and generating sets for marine and industrial installations. We review the engine, generator controls and electrical interfaces together when defining repair, automatic start/stop, synchronisation or power-management requirements for the system.'),
            ('electronics', 'Electronic card repair', 'Repair of electronic control boards used in automation and machinery systems. Assessment starts with the board’s function, equipment model and reported fault, including its power supply and connected signals, to establish the scope of repair.'),
        ],
        'equipment': [
            ('PLC & control', ['Siemens', 'ABB', 'Omron', 'Mitsubishi', 'Allen-Bradley', 'Modicon', 'Honeywell']),
            ('Switchgear & MCC', ['Schneider Electric', 'Siemens', 'GE', 'Areva']),
            ('Drives & soft starters', ['Schneider Electric', 'Rockwell Automation', 'Allen-Bradley', 'ABB']),
            ('Protection relays', ['Sepam 2000', 'Sepam 1000+', 'Areva MiCOM']),
            ('Hazardous area', ['Stahl', 'Chalmit', 'Crouse-Hinds', 'CEAG', 'Glamox', 'Orga']),
            ('Motors', ['Siemens', 'ABB', 'Reliance']),
            ('Transformers, UPS & chargers', ['Unindo', 'Trafindo', 'Saft', 'Gutor', 'GE', 'ICA']),
            ('Generating sets', ['SDMO', 'Denyo', 'Caterpillar', 'Stamford', 'Leroy-Somer']),
            ('Cables & surge protection', ['Jembo', 'Kabelmetal', 'Pirelli', 'Supreme', 'Critec', 'Erico']),
        ],
        'featured': [('comap', 'Engine and generator controllers, power management, InteliSCADA and WebSupervisor monitoring.'),
                     ('noris', 'Sensors, signal processing, limit monitoring and integrated alarm and monitoring systems.')],
        'enquiry': ['Site or vessel and its location', 'Single-line diagram, panel drawings or I/O list', 'PLC/HMI platform and existing program backup, if available', 'Fault description, alarm history or the new functions required', 'Hazardous-area classification, where relevant'],
    },
}
