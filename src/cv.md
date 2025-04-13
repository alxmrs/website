---
description-meta: Alexander Merose is a software engineer and ML researcher focused on ML4Science.
---
<center>

# Alexander S. Merose

<print-only> 
  <ul class="cv-topline">
    <li>SF Bay Area</li>
    <li><a href="https://al.merose.com">al.merose.com</a></li>
    <li>al@merose.com</li> 
  </ul>
</print-only>

</center>

I am a senior software engineer and machine learning researcher. I have played a critical role in two paradigm shifts in
fields of science using machine learning — recently, in [weather prediction](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=9ic0HRsAAAAJ&citation_for_view=9ic0HRsAAAAJ:WF5omc3nYNoC); previously, in [materials science](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=9ic0HRsAAAAJ&citation_for_view=9ic0HRsAAAAJ:d1gkVwhDpl0C). 

<no-print>

_(NB: You can get a curated, 3-page version of this CV my printing the page.)_

</no-print>

# Experience 

<cv-section>

## Founding Member of the Technical Staff, [OpenAthena](https://openathena.ai)

January 2025 - Present. Remote.

</cv-section>

_OpenAthena is a non-profit that helps academic research labs build foundation models for science._

* Assisting [M<sup>2</sup>LInES](https://m2lines.github.io/) build better [ocean-physics emulators](https://github.com/m2lines/Samudra).
* [Dreaming](https://alex.merose.com/pbfft) about platforms for ML and science.


<cv-section>

## Sabbatical 

October 2023 - January 2025

</cv-section>

_I took a gap year with my wife. We traveled the world. Along the way, I worked on a few projects._

<no-print>

<cv-section>

### Writer, vaga • bon • vivants

October 2023 - Present. Remote.

</cv-section>

_We have a travel blog! We’re telling the story of our gap year, one chapter at a time.
[vagabonvivants.com](https://vagabonvivants.com/)_


<cv-section>

### Contributor, [Cubed](https://cubed-dev.github.io/cubed/)

January 2024 - Present. Remote.

</cv-section>

_Cubed is a library for distributed, serverless, memory-bounded computation on the Python Array API._

- [Investigating](https://github.com/cubed-dev/cubed/issues/created_by/alxmrs) how Cubed intersects with accelerators, primarily via JAX.
- Added an affordance for compiling Cubed operations via Numba or JAX (JIT or AOT).
- Adding support for JAX arrays on M1+ hardware via jax-metal.

</no-print>

<cv-section>

### Advisor, [EarthRanger](https://www.earthranger.com/)

January 2024 - June 2024. Remote.

</cv-section>

_EarthRanger is a project funded by the Allen Institute of AI (AI2) to support African Elephant Conservation, among
other conservation projects. It’s a collaborative effort involving the Mara Elephant Project and Ecoscope.io._

- [dask-ee](https://github.com/alxmrs/dask-ee). Google Earth Engine Feature Collections via Dask
  Dataframes. Featured at [SciPy 2024](https://www.youtube.com/watch?v=tH1Dr0iHSxE).
- [xarray-sql](https://github.com/alxmrs/xarray-sql). An experiment to join raster, vector, and point data by
  treating pixels as tables.

<cv-section>

## Anthromet Team, Google Research

2021 - 2023. Remote, CA

</cv-section>

_Anthromet is on a mission to make weather information universally accessible and useful by
developing state-of-the-art AI weather forecasts and integrating them into products._

- [Xee](https://github.com/google/Xee): An Xarray backend for Google Earth Engine. _(Xarray, Google Earth Engine)_
  - Created and launched Xee as a [keynote feature](https://x.com/spatialthoughts/status/1711794831499166032) of [Geo for Good (2023)](/talks#geo-for-good-2023).
  - Part of an internal platform for building AI weather models, this connects GEE to the SciPy ecosystem.
  - Since launch, the library has had ![PyPI Downloads](https://static.pepy.tech/badge/xee) at ![PyPI Downloads](https://static.pepy.tech/badge/xee/month).
- [weather-tools](https://github.com/google/weather-tools).  Pipelines to make weather data universally accessible and useful. Originally a [20%-project](https://en.wikipedia.org/wiki/Side_project_time#Google_implementation), I grew weather-tools to a team of 8 engineers serving ~25 research and product teams across Alphabet _(Apache Beam, Xarray, Google Earth Engine, Google BigQuery)_:
  - [GraphCast](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/): Enabled DeepMind to ingest and regrid ERA5, the dataset behind their autoregressive graph neural network. This was the first AI model to beat physics-based models at predicting the weather. GraphCast was among [2023's top-ten biggest breakthroughs](https://www.science.org/content/article/biggest-science-breakthroughs-2023) published in _Science_, ushering in a new generation of AI-based weather forecasts. 
  - [MetNet v3 & Nowcasting in Google Search](https://blog.research.google/2023/11/metnet-3-state-of-art-neural-weather.html): MetNet is the world’s leading Nowcast, or 24 hour, minute-by-minute weather forecast at 1-4 km resolution. weather-tools created gobal training, inference, and validation datasets, enabling our team to ship to Google Search.
  - [Project Contrails](https://sites.research.google/contrails/). I provided critical weather datasets and pipelines that made this project possible. Project contrails will help address 1% of anthropogenic climate change by reducing solar irradiance from airplanes.
- [Weatherbench2](https://sites.research.google/weatherbench/). The definitive benchmark to fairly compare physics and AI, mid-range weather forecasts and a cornerstone for all future ML weather model development. _(Xarray, Apache Beam, Zarr)_
  - I acquired and cloud-optimized the benchmark's [datasets](https://weatherbench2.readthedocs.io/en/latest/data-guide.html). 
  - I improved [Xarray-Beam](https://github.com/google/xarray-beam), the underlying engine behind the benchmark. 
  - Contributed core benchmark code and helped design the scorecard (a Plotly Dash app!).
- [ARCO-ERA5](https://github.com/google-research/arco-era5). An analysis-ready, cloud-optimized history of weather on Earth. _(Pangeo-Forge, Apache Beam, Xarray, Zarr)_
  - ARCO-ERA5 is the biggest dataset in Cloud Public Datasets, at 12+ petabytes, and likely includes the [biggest single Zarr ever created](https://x.com/shoyer/status/1805735177517416749). 
  - The dataset  has [helped accelerate a boom in AI weather forecasting](https://www.openclimatefix.org/post/lazy-loading-making-it-easier-to-access-vast-datasets-of-weather-satellite-data).
- [Pangeo Forge](https://pangeo-forge.org/). An open ecosystem of data engineering recipes for producing cloud-optimized, analysis ready data. _(Apache Beam, Xarray, Dask, Zarr)_
  - I was a regular contributor to this data engineering system created by the [Pangeo collective](https://pangeo.io/).
  - [I was the impetus](https://github.com/pangeo-forge/pangeo-forge-recipes/issues/256#issuecomment-1026428221) for Pangeo Forge to adopt Apache Beam, for [better](https://medium.com/pangeo/pangeo-forge-is-all-in-on-apache-beam-d7370299405f) or for [worse](https://github.com/pangeo-forge/pangeo-forge-recipes/issues/799#issuecomment-2686467443).
  - Pangeo Forge would go on to cloud optimize [over 4,000 CMIP6 datasets via Apache Beam](https://x.com/JuliusBusecke/status/1781429813258932710).
  - As a part of the project, I contributed a Dask runner to Apache Beam ([and presented it at PyData](https://m.youtube.com/watch?v=uGEQkws1Low)).
- Awards and recognition received while on Anthromet:
  - Google Research’s Science Award for _Best Collaboration_, along with my team and partner teams. 
  - A Greenie award from Anthropocene, an internal grassroots organization focused on climate technologies.
- Lead a team of twelve 20%-engineers to make contributions to the weather community, including internal changes to Google Earth Engine and open source changes to Weather Tools.


<cv-section>

## [Arcs Team](https://github.com/PolymerLabs/arcs), Google Research

2019 – 2021. San Francisco, CA

</cv-section>

_Arcs is an experimental new programming model for privacy-preserving computation and AI. It enables rapid compositional development and probable privacy via data flow analysis. Before the 2023 layoffs, the project internally debuted as a core AI-safety system for ambient computing._

- Extended Arcs data flow analysis system to verify [MediaPipe](https://github.com/google-ai-edge/mediapipe) graphs. This was an important step towards provably private machine learning applications.
- Created a system for automatic claim deduction in a SQL-like subset of the Arcs language. Claim deduction is a core routine to prove that a program adheres to a privacy policy _(Kotlin, Visitor Pattern)_.
- Added features to the project’s domain-specific language; specifically, type variables, maximum-valued types, and reflection. Together, this helped ship a compile-time privacy checking system into production on Android _(Typescript, Kotlin, Data Flow Analysis)_.
- Created a key compiler component to facilitate allocation of modular programs across distributed computing environments, bridging our web technology codebase to Android. _(Typescript, Bazel, Kotlin)_.
- Extended Google’s build system to support Kotlin to Wasm compilation; created code generators to simplify programming with Kotlin on the web _(Kotlin, Wasm, Bazel)_.
- Developed prototypes to discover machine-learning capabilities within the Arcs programming model _(Typescript, Tensorflow JS)_.


<cv-section>

## Machine Learning Engineer, [Aira Tech Corp](https://aira.io/)

2017 – 2019. La Jolla, CA

</cv-section>

_Aira helps blind and low-vision users access visual information via remote assistance with smart glasses._

- Built core dialog engine for an Android Voice-UX. This allowed our blind and low-vision users to pair Bluetooth devices, call a remote assistant, and rate call experiences conversationally. _(Java 8)_
- Created a visual-question-answer research prototype for an NSF grant. The system used real-time object detection and rule-based NLP to investigate assistive user experiences for blind and low vision people. _(Tensorflow, OpenCV, YOLO)_
- Technical lead for prototype of indoor navigation system using computer vision _(OpenSfM, ArcGIS)_.
- Trained and productionized a mobile USD currency classifier model to help blind users identify paper bills. _(Tensorflow, Android, MobileNet, Firebase MLKit)_
- Created an image tagging game to label integral internal datasets. _(Spring Boot, Vue.js, Typescript)_
- Led agile rituals such as daily stand-ups, sprint planning meetings, and retrospectives. Started a machine-learning brownbag lunch series.

<cv-section>

## Research Assistant, [Vecchio Lab](https://kennethvecchioresearchgroup.eng.ucsd.edu/)

2018 – 2019. La Jolla, CA

</cv-section>

_Dr. Vecchio's research group focuses on advanced materials discovery and their translation to industrial applications._

- Used neural networks and boosted tree based algorithms to make materials science discoveries _(Tensorflow/Keras, ResNet, XGBoost, Sklearn)_.
- Applied gradient-based techniques to explain classifications of convolutional neural networks _(GradCam)_.
- Used OOP design principles to create a framework to track hyperparameters & ML pipelines in git.
- Taught nanoengineering graduate students machine learning, focusing on neural networks and tree algorithms.
- The papers produced as a result of my contributions would go on to be published in _Science_, _Nature_, and respected journals within the materials science world.


<cv-section>

## Software Engineer, [Intuit (ProSeries team)](https://accountants.intuit.com/tax-software/proseries/)

2016 – 2017. San Diego, CA

</cv-section>

_ProSeries is intuitive tax-preparation software for tax professionals._

- Reduced rate of application crashes in ProSeries by 50% from prior year via data analysis. _(Python, Pandas)_
- Won business unit hackathon with novel idea for a telemetry system, presented to senior leadership.
- Contributed to annual releases of tax preparation software for legacy Windows application. _(C++, C#)_

<no-print>

<cv-section>

## Software Engineering Intern, [Ingenu](https://www.ingenu.com/)

2016, March - August. San Diego, CA

</cv-section>

_Ingenu is a Internet-Of-Things (IoT) company specializing in low-power, long range networks._
- Developed a single-page web application, adding an RSS feed aggregator and sanitizer (Angular 1, Spring MVC). 
- Reduced application load time by 44% and KB size by 40% via minification, lazy loading, and deployment on a CDN.


<cv-section>

## Founding Frontend Engineer, [Guardiome](https://www.guardiome.com/)

2015 - 2016. La Jolla, CA

</cv-section>

_Guardiome was a dorm-room bioinformatics start-up that provided users a private way to learn about their genome._
- Created a UI engine and interface for an embedded bioinformatics device that allowed users to answer questions about their genome.

<cv-section>

## Software Engineering Intern, [Illumina](https://www.illumina.com/)

2015, July. La Jolla, CA

</cv-section>

_Illumina is a bioinformatics company that produces 90% of the world's genome sequencers._
- Onboarded to creating an Angular 1 progressive web app.
- Fell ill early into the internship and had to leave.

<cv-section>


## Research Assistant, [de Sa Lab](https://pages.ucsd.edu/~desa/)

2013 - 2015. La Jolla, CA

</cv-section>

_de Sa Lab specializes in machine learning and brain computer interfaces (BCI)._
- Developed an [In-Ear EEG prototype](https://www.youtube.com/watch?v=UMACp0fc9TA) aiming to help people with epilepsy. _(OpenBCI, Matlab, SVMs, Ensemble Methods)_
- Developed [BrainTag](https://alxmrs.github.io/BrainTag/), an open source neurofeedback game for children with autism spectrum disorders. Presented at UCSD's Undergrad Research Conference. _(Arduino, Neurosky, C)_
- Initiated collaboration between de Sa lab and [OpenBCI](https://openbci.com/). We were one of the startup’s first university partners.
- Taught open source BCI workshops to UCSD students through hands-on workshops. _(Python, OpenBCI)_
- Wrote data visualization and machine learning toolbox for an open source brain computer interface. _(Python, Java, C, JS)_

</no-print>

# Select Publications

_Please visit my [Google Scholar page](https://scholar.google.com/citations?user=9ic0HRsAAAAJ&hl=en) to see my latest publications._

- **Learning skillful medium-range global weather forecasting**. Remi Lam, Alvaro Sanchez-Gonzalez, Matthew Willson, Peter Wirnsberger, Meire Fortunato, Ferran Alet, Suman Ravuri, Timo Ewalds, Zach Eaton-Rosen, Weihua Hu, **Alexander Merose**, Stephan Hoyer, George Holland, Oriol Vinyals, Jacklynn Stott, Alexander Pritzel, Shakir Mohamed, Peter Battaglia. _Science_ 382 (6677), 1416-1421
- **Discovery of high-entropy ceramics via machine learning**. Kevin Kaufmann, Daniel Maryanovsky, William M Mellor, Chaoyi Zhu, **Alexander S Rosengarten**, Tyler J Harrington, Corey Oses, Cormac Toher, Stefano Curtarolo, Kenneth S Vecchio. _Npj Computational Materials_ 6 (1), 42
- **Crystal symmetry determination in electron diffraction using machine learning**. Kevin Kaufmann, Chaoyi Zhu°, **Alexander S Rosengarten**°, Daniel Maryanovsky, Tyler J Harrington, Eduardo Marin, Kenneth S Vecchio. _Science_ 367 (6477), 564-568
- **WeatherBench 2: A benchmark for the next generation of data‐driven global weather models**. Stephan Rasp, Stephan Hoyer, **Alexander Merose**, Ian Langmore, Peter Battaglia, Tyler Russell, Alvaro Sanchez‐Gonzalez, Vivian Yang, Rob Carver, Shreya Agrawal, Matthew Chantry, Zied Ben Bouallegue, Peter Dueben, Carla Bromberg, Jared Sisk, Luke Barrington, Aaron Bell, Fei Sha. _Journal of Advances in Modeling Earth Systems_ 16 (6), e2023MS004019
- **Deep learning for day forecasts from sparse observations**. Marcin Andrychowicz, Lasse Espeholt, Di Li, Samier Merchant, **Alexander Merose**, Fred Zyda, Shreya Agrawal, Nal Kalchbrenner. _arXiv preprint_ arXiv:2306.06079
- **Deep neural network enabled space group identification in EBSD**. K Kaufmann, C Zhu, **AS Rosengarten**, KS Vecchio. _Microscopy and Microanalysis_ 26 (3), 447-457

_°Equal contribution_

# Technical Skills

<table>
  <tr>
    <th></th>
    <th>Expert</th>
    <th>Proficient</th>
 </tr>
 <tr>
    <td>Language</td>
    <td>Python, Typescript, JS, Kotlin, Java</td>
    <td>C++, C, SQL, Wasm</td>
 </tr>
 <tr>
    <td>Data</td>
    <td>Tensorflow, Xarray, Zarr, NumPy, Dask, Beam, GEE</td>
    <td>JAX, PyTorch, Spark, Parquet, BQ, Postgres</td>
 </tr>
 <tr>
    <td>Product</td>
    <td>GCP, HTML, CSS, Android, REST, Serverless, Docker</td>
    <td>AWS, FastAPI, Express, Spring, VueJS</td>
 </tr>
 <tr>
    <td>Soft</td>
    <td>Leadership, Collaboration, Public Speaking, Empathy</td>
    <td>Agile Rituals, Accessibility, Mentorship</td>
 </tr>

</table>

# Education

B.S. Computer Science, University of California, San Diego, 2011-16 </br>
B.S. Cognitive Science (Computation), University of California, San Diego, 2011-16 </br>
President, [Cognitive Science Student Association](https://cssa-ucsd.org/) </br>
Co-Founder, [Data Science Student Society](https://www.ds3ucsd.com/) </br>
