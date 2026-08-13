## 🛠️ Engineering Update — Landing Gear & Capacity Expansion  
**📅 2026‑08‑10 • 00:55 EDT**
### Summary of Major Revisions
- **Fuselage:** V6 → **V6 Rev6**  
- **Motor Clamp:** V4 (unchanged)  
- **Arm Clamp:** V1 (unchanged)  
- **ESC Clamp:** V1 (unchanged)  
- **New Additions:**
    - Landing Gear System V1(Initial Launch)
    - Expanded Dual‑Battery Bay (72 Ah 12S)
---
<details>
<summary>📷 image</summary>

<img src="https://github.com/user-attachments/assets/cecd8f69-2695-4225-911d-bc4f43c35e75" alt="image" width="600" />
</details>

### 🔧 Major Milestones
- Entered **Fuselage V6 Rev6**, marking the shift toward flight‑ready geometry and subsystem integration.  
- Added a full **landing gear assembly** designed for agricultural UAV operations:  
  - Wide‑stance geometry for stable ground handling  
  - Reinforced mounting plates tied directly into fuselage ribs  
  - Carbon‑rod cross‑members to prevent flex during touchdown  
- Completed expansion of the **battery bay** to support **dual 36 Ah 12S packs in parallel**, enabling:  
  - **Total capacity:** 72 Ah  
  - **Effective discharge:** 20C (2× 10C packs)  
  - Substantially increased endurance for heavy‑lift and long‑route spraying missions  
- Updated internal rib spacing and carbon‑rod bracing to maintain torsional rigidity despite the larger battery footprint.
<table>
<tr>
<td><img src="https://github.com/user-attachments/assets/ee85735d-1556-4028-a0c5-73beaaa3d63c" alt="image" width="600" /></td>
<td><img src="https://github.com/user-attachments/assets/e085f4f1-2857-41b4-b528-efa16fbb68b8" alt="image" width="600" /></td>
<td><img src="https://github.com/user-attachments/assets/6c9f4e64-4df9-45bf-8843-4e8c971b22f9" alt="image" width="600" /></td>
</tr>
</table>
---

### 📐 Structural Improvements
- Battery bay enlargement required adjustments to:  
  - Lower fuselage curvature  
  - Rib cutouts and reinforcement patterns  
  - High‑current cable routing channels for parallel pack leads  
- Landing gear integration introduced:  
  - New load‑bearing sockets bonded to the fuselage spine  
  - Shock‑resistant geometry to reduce vibration transfer into avionics  
- Overall benefits:  
  - Improved CG alignment with dual‑pack configuration  
  - More predictable load paths during landing/takeoff  
  - Cleaner separation between battery bay, ESC corridor, and avionics shelf
---

### 📦 BOM Updates
- Added:  
  - Second Battery  
  - Second AS150u to QS8-S adapter
  - More QS8-S Ports 
- Revised:  
  - PC1500 to PC2500

---

### 🧩 Next Steps
- Validate landing gear under simulated touchdown loads  
- Begin endurance‑focused airflow and cooling analysis for dual‑pack configuration
- Simulate in Gazebo
- Simulate in UE5

---
## 🛠️ Engineering Update — Fuselage V6 Progress & Structural Additions
**📅 2026‑08‑05 • 23:05 EDT**
### Summary of Major Revisions
- Fuselage: V5 → V6
- Motor Clamp: V3 → V4
- Arm Clamp: V1
- ESC Clamp: V1(Initial Release)
---

### 🔧 Major Milestones
- Officially entered **Fuselage V6**
<img width="829" height="594" alt="image" src="https://github.com/user-attachments/assets/5d20b34b-8f17-4e9a-a4ec-7c1b28c99e15" />
- Made ESC mounts
<img width="625" height="559" alt="image" src="https://github.com/user-attachments/assets/b76b1933-6e1f-4b23-8a78-bbbd732ae5d0" />
- Completed **full sectioning of the fuselage**, establishing clear boundaries for:
  - Front module
  - Mid‑section core  
  - Rear module  
- Added new **carbon‑rod reinforcements** to the BOM to increase torsional rigidity and reduce printed‑part load.
  - Includes additional 10x8(OD, ID)mm rods for Internal Ribs  
  - Updated BOM with parts mentioned above, and new filament

---

### 📐 Structural Improvements
- Sectioning the fuselage allowed proper isolation of:
  - Battery bay  
  - ESC cooling corridor  
  - Sensor nose compartment  
  - Rear avionics shelf  
- This segmentation ensures cleaner assembly, easier maintenance, and more predictable load paths.
- Carbon‑rod additions significantly improve stiffness across the fuselage spine and arm sockets.

---

### 🔩 New Component: ESC Clamp (V1)
- Designed and finalized a **new ESC clamp** specifically for the rear module.
- Purpose:
  - Secure ESCs against vibration
  - Mount ESCs Securely

---

### 📦 BOM Updates
- Added:
  - Additional carbon rods (structural + internal bracing)  
  - ESC clamp (printed)  
  - Updated fastener counts for rear module  
- Revised:
  - Fuselage V6 part grouping  
  - Printed plate folder structure  
  - Locking plate documentation

---

### 🧩 Next Steps
  - Wind Tunnel Testing
  - Model Dummy Electronics
  - Model Camera Mounting Holes

  
---

## 🛠️ Engineering Update — Front Fuselage Split (Work in Progress)
**📅 2026‑08‑04 • 22:31 EDT**

---

### 🔧 Current Progress
- Continued splitting the **front fuselage module** into multiple printable sections. The geometry is still being refined, but the main separation planes are established and behaving well.
- Started transitioning from a single large dovetail to **multiple smaller dovetails** along the curved seam. This is already improving alignment and reducing binding during test fits.
- Applied fillets to new edges created by the split. This helps reduce stress concentrations and makes the PA612‑CF geometry print cleaner.
- Continued shaping the **camera‑mount lower housing**. Even though it doesn’t tie into the carbon‑rod frame, internal ribs and supports are being added so it still contributes to front‑section stiffness.
<img width="642" height="451" alt="image" src="https://github.com/user-attachments/assets/f0f373e5-357e-4c8f-8674-02242c4f28e0" />
<img width="920" height="486" alt="image" src="https://github.com/user-attachments/assets/b58c3999-ffcb-4895-a964-7999c09b8e9d" />
<img width="825" height="533" alt="image" src="https://github.com/user-attachments/assets/0dd97be6-8f84-4982-ba7e-a1d09030e151" />

---

### 🚧 Still in Progress
- Finalizing the **battery pack holder** geometry. This will be integrated into the split fuselage once the front section is fully stabilized.
- Additional fillets and internal supports will be added once the battery bay layout is locked in.
- More adjustments expected as the front and bottom sections are test‑printed and checked for fit after funding.

---

## 🛠️ **Engineering Update — Arm Clamp Completion & Fuselage V5 Integration**
**📅 2026‑08‑01 • 12:22 EDT**
### Summary of Major Revisions
- Fuselage: V4 → V5
- Motor Clamp: V3 → V4
- Arm Clamp: V1 (initial release)
---

### 🔧 **Milestone Completed**
- Completed the full CAD for the **V5 arm‑clamp system**, including the revised 40 mm bore, 4 mm structural fillets, and updated geometry for carbon‑rod integration.
- Finalized the **V5 fuselage architecture**, incorporating the new clamp interface, updated arm spacing, and improved structural continuity across the central frame.
- Validated the clamp‑to‑arm transition clearances, ensuring proper fitment for **40×36 mm carbon rods** and eliminating interference caused by earlier oversized fillet radii.

<img width="1077" height="801" alt="image" src="https://github.com/user-attachments/assets/446d2417-757a-41f8-acc7-4102f251cfa5" />


---

### 📐 **Geometric Validation & Structural Improvements**
- Confirmed that the clamp geometry maintains correct alignment with the fuselage’s arm sockets, preserving structural load paths and minimizing stress concentrations at the 40 mm bore.
- Ensured that the 4 mm fillet radius provides adequate reinforcement without interfering with arm geometry or reducing wall thickness around the clamp interface.
- Verified fuselage V5 symmetry, arm spacing, and motor‑mount alignment for the coaxial propulsion layout.
- Updated CAD assemblies to reflect accurate mass properties for clamps, arms, motors, and props prior to infill adjustments.
- Calculated the full V5 assembly mass at **87.2009637 lb (≈39.55 kg)** before hollowing, infill slicing, or internal structural reduction.

---

### 🧩 **Next Steps**
- Begin **internal hollowing** of the fuselage V5 shell to prepare for 30% gyroid infill slicing with 4 walls and 4 floors/roofs.
- Recalculate mass properties after infill reduction to establish accurate flight‑ready weight estimates.
- Integrate **ESC mounting geometry**, wiring channels, and power‑distribution pathways into the fuselage interior.

---

## 🛠️ **Engineering Update — Powertrain & Architecture Overhaul**
**📅 2026‑07‑30 • 22:59 EDT**

---

### 🔧 **Milestone Completed**
- Migrated the propulsion system to **MAD M7C15 IPE motors**, providing higher torque density, improved thermal stability, and IP45‑rated environmental protection suitable for manned‑class reliability.
- Upgraded to a **higher‑current ESC platform**, enabling cleaner transient response, reduced voltage sag, and improved sustained‑thrust performance under heavy load.
- Integrated the **Cube Orange+** flight controller, adding triple‑redundant IMUs, advanced vibration isolation, and expanded sensor‑fusion capabilities for precision flight and safety.
- Converted the airframe to a **coaxial propulsion layout**, increasing total thrust output while reducing arm span and improving yaw authority.
- Updated the master geometry to support **27.2 × 8.9″ propellers**, validating rotor‑disk clearance, coaxial spacing, and aerodynamic interaction between upper and lower rotors.
<img width="1023" height="792" alt="image" src="https://github.com/user-attachments/assets/c4101e4f-68eb-429c-954e-49e03564143b" />
<img width="779" height="724" alt="image" src="https://github.com/user-attachments/assets/f1810303-4bbe-4b42-a029-5617c6fbe6e8" />

(Exploded)

---

### 📐 **Geometric Validation & Structural Improvements**
- Verified that the larger **M7C15 motor housings** fit cleanly within the revised mount architecture, maintaining correct bolt‑circle alignment and ensuring no interference with adjacent structural components.
- Confirmed coaxial spacing meets aerodynamic requirements for:
  - minimized rotor‑wash interference  
  - stable thrust symmetry across the full throttle range  
  - reduced vibration coupling into the flight‑controller bay  
- Validated ESC placement and airflow paths to ensure adequate cooling during peak current draw.
- Updated CAD assemblies to reflect the new motor geometry, ESC footprint, and coaxial stack height, ensuring compatibility with the existing frame and clamp system.

---

### 🧩 **Next Steps**
- Design the **new ESC mounting plate** with improved airflow and vibration isolation.  
- Update the **motor‑clamp reinforcement** to match the increased torque output of the M7C15 motors.  

---

## 🛠️ **Engineering Update — Motor Clamp Wall Reinforcement**
**📅 2026‑07‑28 • 20:36 EDT**

---

### 🔧 **Milestone Completed**
- Increased the **motor‑clamp outer diameter to 55 mm** while maintaining the required **42.7 mm inner diameter** for the 30 mm CF tube + rubber liner stack.
- Achieved a reinforced **6.15 mm wall thickness** (up from 3.65 mm), significantly improving clamp rigidity, torque‑load tolerance, and long‑term structural durability.
- Updated the clamp geometry in the Onshape assembly to ensure seamless integration with the existing motor‑mount layout.
<img width="722" height="663" alt="image" src="https://github.com/user-attachments/assets/b0c23f0b-52bb-4cb9-ab2b-d84afdf989a3" />

---

### 📐 **Geometric Validation & Structural Improvements**
- Verified that the new **55 mm OD** maintains full clearance within the motor‑mount region and does not interfere with adjacent arm geometry.
- Confirmed **6.15 mm wall thickness** meets PA612‑CF print requirements for:
  - torsional resistance under high‑output MAD motors  
  - uniform compression around the 30 mm tube  
  - reduced deformation under sustained thrust loads  
- Revalidated clamp alignment relative to the global horizontal plane to preserve consistent thrust‑vector orientation across all motor positions.

---

### 🧩 **Next Steps**
- Begin hollowing the fuselage interior and define electronics‑bay geometry.
- Add additional clamp variants and determine fuselage split‑line strategy.
- Integrate **arm‑clamp** geometry and validate fit against the updated motor‑clamp dimensions.

---


## 🛠️ **Engineering Update — Motor Mount Integration & Geometry Validation**
**📅 2026‑07‑27 • 22:17 EDT**

---

### 🔧 **Milestone Completed**
- Integrated the **30 mm carbon‑fiber tube motor‑mount clamps** directly into the main Onshape assembly.
- Ensured all mounts sit **perfectly parallel to the global horizontal plane**, guaranteeing uniform downward thrust vectors across the asymmetric V‑Octo layout.

---

### 📐 **Geometric Validation & Layout Specs**
- Verified structural clearance for the **22" (560 mm) MAD HAVOC propellers** using master layout sketches.
- Confirmed pre‑rotor frame wingspan: **≈ 1848.58 mm**.
- Validated asymmetric V‑Octo spacing:
  - Adjacent motor centers maintain a **≥ 110 mm (4.3") rotor‑tip clearance**.
  - Provides safe margin for **blade flex**, **dynamic deflection**, and **manufacturing tolerances**.

---

### 🧩 **Next Steps**
- Hollow out the interior of the fuselage and model where electronics go.
- Add additional clamps, and figure out how to split.
- Add arm clamps.
  
---
