# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

db.define_table('dbcatalog',
                Field('Serial', 'string'),
                Field('Publication_Year', 'integer'),
                Field('PMID', 'string'),
                Field('URL', 'string'),
                Field('Title', 'string'),
                Field('occurrence_initial', 'boolean'),
                Field('occurrence_update', 'boolean'),
                Field('taxonomy_single_strain', 'boolean'),
                Field('taxonomy_single_species', 'boolean'),
                Field('taxonomy_multi_species', 'boolean'),
                Field('taxonomy_virus', 'boolean'),
                Field('taxonomy_eubacteria', 'boolean'),
                Field('taxonomy_archaebacteia', 'boolean'),
                Field('taxonomy_eukaryotes', 'boolean'),
                Field('taxonomy_mammals', 'boolean'),
                Field('taxonomy_model_organism', 'boolean'),
                Field('taxonomy_human', 'boolean'),
                Field('taxonomy_invertebrate', 'boolean'),
                Field('taxonomy_vertebrate', 'boolean'),
                Field('taxonomy_unicellular_eukaryotes', 'boolean'),
                Field('taxonomy_plants', 'boolean'),
                Field('taxonomy_fungi', 'boolean'),
                Field('data_single_molecule_type', 'boolean'),
                Field('data_DNA', 'boolean'),
                Field('data_RNA', 'boolean'),
                Field('data_protein', 'boolean'),
                Field('data_lipids', 'boolean'),
                Field('data_carbohydrates', 'boolean'),
                Field('data_chemicals_and_small_molecules', 'boolean'),
                Field('data_genes', 'boolean'),
                Field('data_genome', 'boolean'),
                Field('data_transcriptome', 'boolean'),
                Field('data_proteome', 'boolean'),
                Field('data_metabolome', 'boolean'),
                Field('data_structure', 'boolean'),
                Field('data_sequence', 'boolean'),
                Field('data_short_tandem_repeats', 'boolean'),
                Field('data_intron_exon', 'boolean'),
                Field('data_coding_non_coding_DNA', 'boolean'),
                Field('data_complements', 'boolean'),
                Field('data_transposons', 'boolean'),
                Field('data_promoters_and_regulators', 'boolean'),
                Field('data_metal_ion_binding_interactions', 'boolean'),
                Field('data_enzymatic_sites_complexes', 'boolean'),
                Field('data_localization', 'boolean'),
                Field('data_motif', 'boolean'),
                Field('data_classification', 'boolean'),
                Field('data_genetic_similarity_and_or_conservation', 'boolean'),
                Field('data_properties_and_annotation', 'boolean'),
                Field('data_enzymes', 'boolean'),
                Field('data_ribozymes', 'boolean'),
                Field('data_pathways', 'boolean'),
                Field('data_protein_nucleic_acid_interactions', 'boolean'),
                Field('data_protein_protein_interactions', 'boolean'),
                Field('data_post_translational_modifications', 'boolean'),
                Field('data_diseases', 'boolean'),
                Field('data_mutations_and_polymorphisms', 'boolean'),
                Field('data_probes_and_primers', 'boolean'),
                Field('data_antibodies', 'boolean'),
                Field('data_ligand_activity_and_pairs', 'boolean'),
                Field('data_drugs_and_drug_targets', 'boolean'),
                Field('data_clinical', 'boolean'),
                Field('data_literature', 'boolean'),
                Field('data_statistics', 'boolean'),
                Field('data_ancient', 'boolean'),
                Field('data_comparative', 'boolean'),
                Field('data_high_throughput', 'boolean'),
                Field('data_microarray', 'boolean'),
                Field('data_NGS', 'boolean'),
                Field('data_crystallography', 'boolean'),
                Field('data_mass_spectrometry', 'boolean'),
                Field('data_images', 'boolean'),
                Field('data_images_microscopic', 'boolean'),
                Field('data_model', 'boolean'),
                Field('data_model_3D', 'boolean'),
                Field('data_model_interactions', 'boolean'),
                Field('data_inferred', 'boolean'),
                Field('system_organelles', 'boolean'),
                Field('system_nucleus', 'boolean'),
                Field('system_cytoplasm', 'boolean'),
                Field('system_mitochondria', 'boolean'),
                Field('system_chloroplast', 'boolean'),
                Field('system_ribosome', 'boolean'),
                Field('system_extracellular', 'boolean'),
                Field('system_whole_cell', 'boolean'),
                Field('system_tissues', 'boolean'),
                Field('system_organs', 'boolean'),
                Field('system_organ_systems', 'boolean'),
                Field('system_organism', 'boolean'),
                Field('system_population', 'boolean'),
                Field('access_web_forms_applications', 'boolean'),
                Field('access_programmatic', 'boolean'),
                Field('access_data_download', 'boolean'),
                Field('access_submission', 'boolean'),
                Field('status_alive', 'boolean'),
                Field('status_dead', 'boolean'),
                Field('status_unknown', 'boolean')
                )

auth.enable_record_versioning(db)
