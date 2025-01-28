---
title: Notes on "A Comparison of Neuroelectrophysiology Databases"
date: 2025-01-27T09:59
description-meta: 
status: 
tags:
  - neuro
  - python
  - programming
  - data-type
  - arco
  - oss
  - science
---
Paper compares 4 intracranial neuroelectrophysiology "data repositories" (read: data formats):
- DABI: Data Archive for the BRAIN Initiative
- DANDI: Distributed Archives for Neurophysiological Data Integration
- OpenNeuro
- Brain CODE
These two efforts also utilize NWB (Neurodata Without Borders) and BIDS (Brain Imaging Data Structure).

The paper calls this field "neuroinformatics." I really like that. 

One reason there's more iEEG (intercranial EEG) data available these days is due to FDA approval of DBS (Deep Brain Stimulation) therapies in the last three decades. 

Because this data is produced for primarily medical reasons, they often also imply other forms of multi-modal imaging. For example, imaging is likely taken in order to know where to properly place electrodes. This leads to richer datasets. 

Because these surgeries are so invasive and expensive, the production of such neural data is quite rare. Thus, centralized datasets and data standards are really important for the advancement of the field. 

EEGLAB (from UCSD) and OpenNeuro (from Stanford) created NEMAR, the Neuroelectromagnetic Data Archive and Tools Resource, in 2019.

[NIMH Data Archive](https://nda.nih.gov/): _National Institute of Mental Health_ Data Archive. Makes data from human subjects across many scientific domains anonymous and available. Not all data is publicly available; many datasets have strict access requirements. 

Data governance definition (emphasis mine):

> Data governance is critical in well-established archive management and data asset control. It involves establishing frameworks that dictate how data are collected, stored, accessed, shared, and organized. **In the context of data archives, data governance oversees the entire archival process, encompassing data retention policies, security measures, access controls, and data integrity and privacy.**


DANDI: a 2019 repository of neurophysiology and neuroimaging datasets (i.e. "Dandisets") for human and non-human data. Led by scientists at MIT and Dartmouth. Intended to aid in the adoption of BIDS, NWB, and NIDM (Neuroimaging Data Model). Includes W3C Provenance data (W3C-PROV). 

OpenNeuro was developed from OpenFRMI.org. 

HED: Hierarchical Event Descriptors. It's what NEMAR uses in addition to BIDS. 


On file formats (emphasis mine): 

> A variety of neurophysiology data modalities (i.e., EEG, MEG, DBS, and iEEG) results in a wide range of formats and structures, leading to challenges in integrating and analyzing pooled data. **The lack of standardization of recorded file formats complicates building large-scale datasets and requires file conversion.** The emergence of intracranial neurophysiology databases necessitated improved standardization and harmonization protocols to ensure data usability and integration. DABI, DANDI, OpenNeuro, and Brain-CODE offer nuanced solutions to address this demand.

BIDS is becoming the leading standard for harmonizing imaging data. 

BIDS abstracts common metadata across different imaging modalities, where each modality has its own data format (and history). 

On NWB vs BIDS
- More common for cellular data, not as much for EEG or MEG
- NWB requires conversion of underlying format within a NWB file, unlike BIDS, which allows modality-specific formats.
- The benefit of the host cost (conversion) is standardization, data chunking and standard (lossless) compression.

DANDI's platform requires data uploaders to adhere to data standards. Cellular data is usually NWB; optical physiology uses OME-Zarr for microscopy. Dandisets must adhere to BIDS-like lightweight file tree hierarchy -- as provided by the dandi CLI. BIDS is required for neuroimaging data (like structural MRI, fMRI). Metadata standards follow NIDM. The team helps both NWB and BIDS in developing standards. 


They point out this inherent tradeoff between strict and loose adhereance to neuro data standards: 

> Some archives strictly adhere to standardization protocols, while others offer more flexibility in accepted data formats. Data standards make harmonization less challenging but may limit the amount of collected data. On the other hand, accepting a broader range of formats creates a harmonization hurdle. One solution is to accept formats that can be converted into multiple acceptable data structures (e.g., BIDS or NWB). While indiscriminate acceptance reduces time-consuming conversions by providers, it leaves the harmonization task to users.

IMO, this is where Zarr Virtualization may really deliver a good solution. What if the code complexity and storage costs of data conversion was low? 


Beyond standards, data sharing "protocols" limits analysis: 

> Many researchers elect to keep their datasets or metadata private, while others upload incomplete sets, hindering the reanalysis efforts. Some repositories allow data owners to upload agreements that require co-authorship considerations, provide guidelines on crediting the sets, and outline stipulations before releasing the data. BRAIN Initiative’s guidelines for data sharing have continued to improve by adapting to the needs of the data providers and users, removing ambiguity, and offering a policy that can be uniformly implemented to enhance data sharing in this field further.

The Canadian's Brain-CODE project mandates that data collected with their funding has to be made option: 

> In Canada, OBI mandates that all Integrated Discovery (“ID”) Programs it funds provide data to Brain-CODE to foster collaboration and data sharing. Therefore, OBI’s policy on data sharing states that the data produced through its funding should be accessible with minimal constraints in a responsible and timely manner


The paper says that the existing data sharing efforts have led to successes in Alzheimer's treatment. That's excellent!!

The paper calls out standard data collection processes, not just post-processing standards, since post-processing can reduce the underlying signal.

On standardization:
> Furthermore, limiting the number of possible file formats or proposing a universal format would eliminate the need for file harmonization. 

Maybe Zarr could be that file format!

---
# References

https://pmc.ncbi.nlm.nih.gov/articles/PMC10327244/

![A Comparison of Neuroelectrophysiology Databases](nihpp-2306.15041v2.pdf)