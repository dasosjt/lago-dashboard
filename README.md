# Lago Dashboard


## The LAGO Project

> "The LAGO (Latin American Giant Observatory) project is an extended Astroparticle Observatory at global scale. It is mainly oriented to basic research on three branches of Astroparticle physics: the Extreme Universe, Space Weather phenomena, and Atmospheric Radiation at ground level.

>The LAGO detection network consists in single or small arrays of particle detectors at ground level, spanning over different sites located at significantly different latitudes (currently from Mexico up to the Antarctic region) and different altitudes (from sea level up to more than 5000 meters over sea level), covering a huge range of geomagnetic rigidity cut-offs and atmospheric absorption/reaction levels.

>The LAGO Project is operated by the LAGO Collaboration, a non-centralized and distributed collaborative network of more than 80 scientist from more than 25 institutions of 9 latinamerican countries (currently Argentina, Bolivia, Brazil, Colombia, Ecuador, Mexico, Peru and Venezuela. See the complete list of the collaboration members and their institutions).

>Finally, detectors installed in various universities are used as a tool to teach students about particle and astroparticle physics, in particular by leading them to the measurement of the muon decay. " <http://lagoproject.org/>

As the final statement establish, this repo contains the code to execute a dashboard that filters the results from here, in Guatemala, as part of a project in the University del Valle de Guatemala. 

## Project Setup

### Python

Create virtualenv with python3 at backend root folder

`virtualenv -p python3 ld-env`

Load virtualenv bash script

`source ld-env/bin/activate`

Install project app requirements

`pip install -r requirements.txt`

### Check Hive connection

Establish th hive connection through any cluster node to retrieve results to display.

gtlagom01.uvg.edu.gt
gtlagow01.uvg.edu.gt
gtlagow02.uvg.edu.gt

### Debug mode

for debug mode set DEBUG=TRUE as enviroment variable. This will indicate to use the results from ./static folder.

## Project startup

After initializing the enviroment and take source from ./ld-env/bin/activate, you can start the project:

`python app.py`