# Curriculum vitae

I am a senior software engineer focused on machine learning. I have played a critical role in two paradigm shifts in
fields of science using machine learning — first, in materials characterization & discovery; second, in weather prediction.

I do my best work in highly collaborative environments. As much as possible, I try to contribute to open source.

# Sabbatical Projects

## Writer, vaga • bon • vivants

October 2023 - Present. Remote.

_My wife and I have a travel blog! We’re telling the story of our gap year, one chapter at a time.
[vagabonvivants.com](https://vagabonvivants.com/)_

## Contributor, [Cubed](https://cubed-dev.github.io/cubed/)

January 2024 - Present. Remote.

_Cubed is a library for distributed, serverless, memory-bounded computation on the Python Array API._

- Investigating how Cubed intersects with accelerators, primarily via JAX.
- Added an affordance for compiling Cubed operations via Numba or JAX (JIT or AOT).
- Adding support for JAX arrays on M1+ hardware via jax-metal.

## Advisor, [EarthRanger](https://www.earthranger.com/)

January 2023 - June 2024. Remote.

_EarthRanger is a project funded by the Allen Institute of AI (AI2) to support African Elephant Conservation, among
other conservation projects. It’s a collaborative effort involving the Mara Elephant Project and Ecoscope.io._

- [github.com/alxmrs/xarray-sql](https://github.com/alxmrs/xarray-sql/). What if we could join raster and vector data by
  treating pixels as tables?
- [github.com/alxmrs/dask-ee](https://github.com/alxmrs/dask-ee). Google Earth Engine Feature Collections via Dask
  Dataframes.
    - The library was presented by [Quisheng Wu at SciPy 2024](https://www.youtube.com/watch?v=tH1Dr0iHSxE).

# Google Experience

## Anthromet Team, Google Research

2021 - 2023. Remote, CA

_Anthromet is on a mission to make weather information universally accessible and useful. It does this by enabling the
development of state-of-the-art AI forecasts and integrating them into products._

- [Weather Tools](https://github.com/google/weather-tools), a set of data pipelines to make weather data universally accessible and useful. _(Apache Beam, Xarray, Google Earth Engine, Google BigQuery, MetView)_. Originally a 20% effort, I grew the project to a team of 8 engineers to serve ~22 research and product teams across Google AI, Brain, X, DeepMind and Cloud. Some highlights:
  - [GraphCast](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/): these tools enabled DeepMind to ingest and regrid ERA5, the dataset behind their autoregressive graph neural network. At the time of publishing, this was the SOTA 10 day weather forecast, beating physics based models. GraphCast was published in Science and has ushered in a new generation of AI-based weather forecasting. The model is being adopted by ECMWF. 
  - [MetNet v3 & Nowcasting in Google Search](https://blog.research.google/2023/11/metnet-3-state-of-art-neural-weather.html): MetNet is the world’s leading Nowcast, or 24 hour, minute by minute weather forecast at 1-4 km resolution. Weather-Tools were used to ingest a global weather training and validation dataset for the development of this model as well as for production inference in Google Search (especially in the EU). `weather-mv` focuses on ingesting weather data into Google Earth Engine in batch and in real time.
  - [Project Contrails](https://sites.research.google/contrails/). I provided critical weather data and data engineering pipelines that made this project possible. This project alone will solve 1% of anthropogenic climate change by reducing solar irradiance from airplanes. 
  - [ARCO-ERA5](https://github.com/google-research/arco-era5) & [Weatherbench2](https://sites.research.google/weatherbench/): I ingested and published the two biggest datasets in Google Cloud’s Public Dataset program. These petabytes of data were cloud optimized as Zarr. I worked with Cloud to shape weather tools to ingest ERA5 into Google BigQuery.
  - [SEEDS](https://blog.research.google/2024/03/generative-ai-to-quantify-uncertainty.html). Provided data coordinate and support for this GenAI ensemble weather forecast (diffusion modeling). SEEDS makes it possible to predict rarer weather events or predict at higher resolutions over physics based methods since the ML approach creates a surplus of compute. 
  - [DeepMind’s Wind Energy optimization](https://deepmind.google/discover/blog/machine-learning-can-boost-the-value-of-wind-energy/). By ingesting weather data from the ECMWF into Google BigQuery, I was able to help create an ML model with DeepMind and Cloud to make wind energy more profitable in the Texas energy grid. This was the original 20% project motivating weather tools. The ECMWF data and ingestion system lead to a ~3% improvement of mean absolute zero error compared to benchmarks. This led to ~$7 million more in revenue over 8 months from wind power.
- [Weatherbench2](https://sites.research.google/weatherbench/). WB2 is the definitive benchmark to fairly compare AI-based, mid-range weather forecasts. This is ushering in a new generation of ML weather forecasting. _(Xarray, Apache Beam, Zarr)_
  - Besides ingesting the fundamental datasets (see above), I made core updates to Xarray-Beam, the underlying engine behind the benchmark. 
  - Contributed code to the benchmark itself, helping ship it to production. 
- [Xee](https://github.com/google/Xee): An Xarray backend for Google Earth Engine. _(Xarray, Google Earth Engine)_
  - Creator of this package. Launched as a keynote feature of Geo for Good 2023. 
  - This bridges Google Earth Engine and the scientific Python communities (i.e.  Xarray users).
  - Internally, this was a key component of a weather research platform to create new weather models and help put them into production.
  - Between 2023-10-11 and 2024-08-07, Xee received [52k downloads, including 8k downloads a month](https://www.pepy.tech/projects/xee) on Pip. 
- [ARCO-ERA5](https://github.com/google-research/arco-era5) & [Pangeo Forge](https://pangeo-forge.org/). _(Apache Beam, Xarray, Zarr)_
  - Pangeo Forge is aiming to become the conda-forge of scientific datasets, or open ecosystem of data engineering recipes for producing cloud-optimized, analysis ready data.
  - I was the impetus for the Pangeo Forge Project to transition their data engineering core system to Apache Beam.
  - I contributed bug fixes and the Beam integration upstream to Pangeo Forge to produce ARCO-ERA5. 
  - ARCO-ERA5 is the biggest dataset in cloud public datasets, at 3-6 petabytes. It represents the most accurate history of weather on Earth from 1940 to the present. 
  - We produced cloud optimized and analysis ready data in the Zarr format, making this critical dataset accessible to everyone (especially, ML algorithms). 
  - To support the Pangeo Forge project, I contributed Dask runner support to the Apache Beam project ([presented at PyData NYC](https://m.youtube.com/watch?v=uGEQkws1Low)).
  - Pangeo Forge would go on to cloud optimize over 4,000 CMIP6 datasets via Apache Beam.
- Awards and recognition received while on Anthromet:
  - Google Research’s Science Award for _Best Collaboration_, along with my team and several partner teams. 
  - A Greenie award from Anthropocene, an internal grassroots organization focused on climate technologies.
  - A spot bonus from John Platt, the head of Google Applied Sciences, for speeding up a critical data ingestion workflow by a few orders of magnitude. 
- Lead a team of twelve 20%-engineers to make contributions to the weather community, including internal changes to Google Earth Engine and open source changes to Weather Tools.

## [Arcs Team](https://github.com/PolymerLabs/arcs), Google Research

2019 – 2021. San Francisco, CA

_Arcs is an experiment attempting to create a new programming model for privacy-preserving computation and AI. It enables rapid compositional development and probable privacy via data flow analysis. Before the 2023 layoffs, the project internally debuted as a core AI-safety system for ambient computing._

- Extended Arcs data flow analysis system to verify MediaPipe graphs. This was an important step towards provably private machine learning applications.
- Created a system for automatic claim deduction in a SQL-like subset of the Arcs language. Claim deduction is a core routine to prove that a program adheres to a privacy policy _(Kotlin, Visitor Pattern)_.
- Added features to the project’s domain-specific language; specifically, type variables, maximum-valued types, and reflection. Together, this helped ship a compile-time privacy checking system into production on Android _(Typescript, Kotlin, Data Flow Analysis)_.
- Created a key compiler component to facilitate allocation of modular programs across distributed computing environments, bridging our web technology codebase to Android. _(Typescript, Bazel, Kotlin)_.
- Extended Google’s build system to support Kotlin to Wasm compilation; created code generators to simplify programming with Kotlin on the web _(Kotlin, Wasm, Bazel)_.
- Developed prototypes to discover machine-learning capabilities within the Arcs programming model _(Typescript, Tensorflow JS)_.

# Pre-Google Experience

## Machine Learning Engineer, [Aira Tech Corp](https://aira.io/)

2017 – 2019. La Jolla, CA

_Aira helps blind and low-vision users access visual information via remote assistance with smart glasses._

- Built core dialog engine for an Android Voice-UX. This allows our blind and low-vision users to pair Bluetooth devices, call a remote assistant, and rate call experiences conversationally. _(Java 8)_
- Created a visual-question-answer research prototype for an NSF grant. The system used real-time object detection and rule-based NLP to investigate assistive user experiences for blind and low vision people. _(Tensorflow, OpenCV, YOLO)_
- Technical lead for prototype of indoor navigation system based on Open Structure-from-Motion, Android, and ArcGIS.
- Trained and productionized a mobile USD currency classifier model to help blind users identify paper bills. _(Tensorflow, Android, MobileNet, Firebase MLKit)_
- Led agile rituals such as daily stand-ups, sprint planning meetings, and retrospectives.

## Research Assistant, [Vecchio Lab](https://kennethvecchioresearchgroup.eng.ucsd.edu/)

2018 – 2019. UCSD Nanoengineering Department. La Jolla, CA

_Dr. Vecchio's research group focuses on advanced materials discovery and their translation to industrial applications._

- Used neural networks and boosted tree based algorithms to make materials science discoveries _(Keras, ResNet, XGBoost, Sklearn)_.
- Applied gradient-based techniques to explain classifications of convolutional neural networks _(GradCam)_.
- Used OOP design principles to create a framework to track hyperparameters & ML pipelines in version control.
- Taught nanoengineering grad students machine learning, focusing on neural networks and tree-based techniques.
- The papers produced as a result of my contributions would go on to be published in Science, Nature, and respected journals within the materials science world.

## Software Engineer, [Intuit (ProSeries team)](https://accountants.intuit.com/tax-software/proseries/)

2016 – 2017. San Diego, CA

_ProSeries is intuitive tax-preparation software for tax professionals._

- Lead data-oriented effort to reduce the number of application crashes in ProSeries by 50% from prior year. _(Python, Pandas)_
- Contributed to annual releases of tax preparation software for legacy Windows application. _(C++, C#)_
- Invented C-macro-preprocessor method to eliminate year-over-year maintenance work.

## Software Engineering Intern, [Ingenu](https://www.ingenu.com/)

2016, March - August. San Diego, CA

_Ingenu is a Internet-Of-Things (IoT) company specializing in low-power, long range networks._
- Developed a single-page web application, adding an RSS feed aggregator and sanitizer (Angular 1, Spring MVC). 
- Reduced application load time by 44% and KB size by 40% via minification, lazy loading, and deployment on a CDN.

## Founding Frontend Engineer, [Guardiome](https://www.guardiome.com/)

2015 - 2016. La Jolla, CA

_Guardiome was a dorm-room bioinformatics start-up that provided users a private way to learn about their genome._
- Created a UI engine and interface for an embedded bioinformatics device that allowed users to answer questions about their genome. 

## Software Engineering Intern, [Illumina](https://www.illumina.com/)

2015, July. La Jolla, CA

_Illumina is a bioinformatics company that produces 90% of the world's genome sequencers._
- Onboarded to creating an Angular 1 progressive web app.
- Fell ill early into the internship and had to leave.

## Research Assistant, [Natural Computation Laboratory (de Sa Lab)](https://pages.ucsd.edu/~desa/)

2013 - 2015. UCSD CogSci Department. La Jolla, CA

_de Sa Lab specializes in machine learning and brain computer interfaces (BCI)._
- Developed an [In-Ear EEG prototype](https://www.youtube.com/watch?v=UMACp0fc9TA) aiming to help people with epilepsy. _(OpenBCI, Matlab, SVMs, Ensemble Methods)_
- Developed [BrainTag](https://alxmrs.github.io/BrainTag/), an open source neurofeedback game for children with autism spectrum disorders. _(Arduino, Neurosky, C)_
- Initiated collaboration between de Sa lab and [OpenBCI](https://openbci.com/). We were one of the startup’s first research collaborators.
- Taught open source BCI workshops to UCSD students through hands-on workshops. _(Python, OpenBCI)_
- Wrote data visualization and machine learning toolbox for an open source brain computer interface. _(Python, Java, C, JS)_

# Publications

_Please visit my [Google Scholar page](https://scholar.google.com/citations?user=9ic0HRsAAAAJ&hl=en) to see my latest publications._

- **Learning skillful medium-range global weather forecasting**. Remi Lam, Alvaro Sanchez-Gonzalez, Matthew Willson, Peter Wirnsberger, Meire Fortunato, Ferran Alet, Suman Ravuri, Timo Ewalds, Zach Eaton-Rosen, Weihua Hu, **Alexander Merose**, Stephan Hoyer, George Holland, Oriol Vinyals, Jacklynn Stott, Alexander Pritzel, Shakir Mohamed, Peter Battaglia. _Science_ 382 (6677), 1416-1421
- **Discovery of high-entropy ceramics via machine learning**. Kevin Kaufmann, Daniel Maryanovsky, William M Mellor, Chaoyi Zhu, **Alexander S Rosengarten**, Tyler J Harrington, Corey Oses, Cormac Toher, Stefano Curtarolo, Kenneth S Vecchio. _Npj Computational Materials_ 6 (1), 42
- **Crystal symmetry determination in electron diffraction using machine learning**. Kevin Kaufmann, Chaoyi Zhu, **Alexander S Rosengarten**, Daniel Maryanovsky, Tyler J Harrington, Eduardo Marin, Kenneth S Vecchio. _Science_ 367 (6477), 564-568
- **WeatherBench 2: A benchmark for the next generation of data‐driven global weather models**. Stephan Rasp, Stephan Hoyer, **Alexander Merose**, Ian Langmore, Peter Battaglia, Tyler Russell, Alvaro Sanchez‐Gonzalez, Vivian Yang, Rob Carver, Shreya Agrawal, Matthew Chantry, Zied Ben Bouallegue, Peter Dueben, Carla Bromberg, Jared Sisk, Luke Barrington, Aaron Bell, Fei Sha. _Journal of Advances in Modeling Earth Systems_ 16 (6), e2023MS004019
- **Deep learning for day forecasts from sparse observations**. Marcin Andrychowicz, Lasse Espeholt, Di Li, Samier Merchant, **Alexander Merose**, Fred Zyda, Shreya Agrawal, Nal Kalchbrenner. _arXiv preprint_ arXiv:2306.06079
- **Deep neural network enabled space group identification in EBSD**. K Kaufmann, C Zhu, **AS Rosengarten**, KS Vecchio. _Microscopy and Microanalysis_ 26 (3), 447-457


# Education

B.S. Computer Science, University of California, San Diego, 2011-16 </br>
B.S. Cognitive Science (Computation), University of California, San Diego, 2011-16 </br>
President, [Cognitive Science Student Association](https://cssa-ucsd.org/) </br>
Co-Founder, [Data Science Student Society](https://www.ds3ucsd.com/) </br>
