# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

@auth.requires_login()
def search():
    table = [TR(H5('Category: Occurrence')),
             TR('', INPUT(_type='checkbox', _name='occurrence_initial'), 'Initial', '',
                    INPUT(_type='checkbox', _name='occurrence_update'), 'Update'),
             TR(H5('Category: Taxonomy')),
             TR('', INPUT(_type='checkbox', _name='taxonomy_single_strain'), 'Single Strain', '',
                    INPUT(_type='checkbox', _name='taxonomy_single_species'), 'Single Species', '',
                    INPUT(_type='checkbox', _name='taxonomy_multi_species'), 'Multi-Species'),
             TR('', INPUT(_type='checkbox', _name='taxonomy_virus'), 'Virus', '',
                    INPUT(_type='checkbox', _name='taxonomy_eubacteria'), 'Eubacteria', '',
                    INPUT(_type='checkbox', _name='taxonomy_archaebacteia'), 'Archaebacteria'),
             TR('', INPUT(_type='checkbox', _name='taxonomy_eukaryotes'), 'Eukaryotes', '',
                    INPUT(_type='checkbox', _name='taxonomy_mammals'), 'Mammals', '',
                    INPUT(_type='checkbox', _name='taxonomy_model_organism'), 'Model Organisms'),
             TR('', INPUT(_type='checkbox', _name='taxonomy_human'), 'Human', '',
                    INPUT(_type='checkbox', _name='taxonomy_invertebrate'), 'Invertebrate', '',
                    INPUT(_type='checkbox', _name='taxonomy_vertebrate'), 'Vertebrate'),
             TR('', INPUT(_type='checkbox', _name='taxonomy_unicellular_eukaryotes'), 'Unicellular Eukaryotes', '',
                    INPUT(_type='checkbox', _name='taxonomy_plants'), 'Plants', '',
                    INPUT(_type='checkbox', _name='taxonomy_fungi'), 'Fungi'),
             TR(H5('Category: Type of Data')),
             TR('', INPUT(_type='checkbox', _name='data_single_molecule_type'), 'Single Molecule', '',
                    INPUT(_type='checkbox', _name='data_DNA'), 'DNA', '',
                    INPUT(_type='checkbox', _name='data_RNA'), 'RNA'),
             TR('', INPUT(_type='checkbox', _name='data_protein'), 'Protein', '',
                    INPUT(_type='checkbox', _name='data_lipids'), 'Lipids', '',
                    INPUT(_type='checkbox', _name='data_carbohydrates'), 'Carbohydrates'),
             TR('', INPUT(_type='checkbox', _name='data_genes'), 'Genes', '',
                    INPUT(_type='checkbox', _name='data_genome'), 'Genome', '',
                    INPUT(_type='checkbox', _name='data_chemicals_and_small_molecules'), 'Chemicals and Small Molecules'),
             TR('', INPUT(_type='checkbox', _name='data_transcriptome'), 'Transcriptome', '',
                    INPUT(_type='checkbox', _name='data_proteome'), 'Proteome', '',
                    INPUT(_type='checkbox', _name='data_metabolome'), 'Metabolome'),
             TR('', INPUT(_type='checkbox', _name='data_structure'), 'Structure', '',
                    INPUT(_type='checkbox', _name='data_sequence'), 'Sequence', '',
                    INPUT(_type='checkbox', _name='data_short_tandem_repeats'), 'Short Tandem Repeats'),
             TR('', INPUT(_type='checkbox', _name='data_intron_exon'), 'Intron/Exon', '',
                    INPUT(_type='checkbox', _name='data_complements'), 'Complements', '',
                    INPUT(_type='checkbox', _name='data_coding_non_coding_DNA'), 'Coding/Non-Coding DNA'),
             TR('', INPUT(_type='checkbox', _name='data_transposons'), 'Transposons', '',
                    INPUT(_type='checkbox', _name='data_localization'), 'Localization', '',
                    INPUT(_type='checkbox', _name='data_promoters_and_regulators'), 'Promoters and Regulators'),
             TR('', INPUT(_type='checkbox', _name='data_motif'), 'Motif', '',
                    INPUT(_type='checkbox', _name='data_classification'), 'Classification', '',
                    INPUT(_type='checkbox', _name='data_metal_ion_binding_interactions'), 'Metal Ion Binding Interactions'),
             TR('', INPUT(_type='checkbox', _name='data_enzymatic_sites_complexes'), 'Enzymatic Sites Complexes', '',
                    INPUT(_type='checkbox', _name='data_properties_and_annotation'), 'Properties and Annotation', '',
                    INPUT(_type='checkbox', _name='data_genetic_similarity_and_or_conservations'), 'Genetic Similarity and/or Conservation'),
             TR('', INPUT(_type='checkbox', _name='data_enzymes'), 'Enzymes', '',
                    INPUT(_type='checkbox', _name='data_ribozymes'), 'Ribozymes', '',
                    INPUT(_type='checkbox', _name='data_protein_nucleic_acid_interactions'), 'Protein-Nucleic Acid Interactions'),
             TR('', INPUT(_type='checkbox', _name='data_pathways'), 'Pathways', '',
                    INPUT(_type='checkbox', _name='data_post_translational_modifications'), 'Post-Translational Modifications', '',
                    INPUT(_type='checkbox', _name='data_protein_protein_interactions'), 'Protein-Protein Interactions'),
             TR('', INPUT(_type='checkbox', _name='data_diseases'), 'Diseases', '',
                    INPUT(_type='checkbox', _name='data_probes_and_primers'), 'Probes and Primers', '',
                    INPUT(_type='checkbox', _name='data_mutations_and_polymorphisms'), 'Mutations and Polymorphisms'),
             TR('', INPUT(_type='checkbox', _name='data_antibodies'), 'Antibodies', '',
                    INPUT(_type='checkbox', _name='data_clinical'), 'Clinical', '',
                    INPUT(_type='checkbox', _name='data_ligand_activity_and_pairs'), 'Ligand Activity and Pairs'),
             TR('', INPUT(_type='checkbox', _name='data_literature'), 'Literature', '',
                    INPUT(_type='checkbox', _name='data_statistics'), 'Statistics', '',
                    INPUT(_type='checkbox', _name='data_drugs_and_drug_targets'), 'Drugs and Drug Targets'),
             TR('', INPUT(_type='checkbox', _name='data_ancient'), 'Ancient', '',
                    INPUT(_type='checkbox', _name='data_comparative'), 'Comparative', '',
                    INPUT(_type='checkbox', _name='data_high_throughput'), 'High Throughput'),
             TR('', INPUT(_type='checkbox', _name='data_microarray'), 'Microarray', '',
                    INPUT(_type='checkbox', _name='data_crystallography'), 'Crystallography', '',
                    INPUT(_type='checkbox', _name='data_NGS'), 'Next Generation Sequencing'),
             TR('', INPUT(_type='checkbox', _name='data_mass_spectrometry'), 'Mass Spectrometry', '',
                    INPUT(_type='checkbox', _name='data_images'), 'Images', '',
                    INPUT(_type='checkbox', _name='data_images_microscopic'), 'Microscopic Images'),
             TR('', INPUT(_type='checkbox', _name='data_model'), 'Model', '',
                    INPUT(_type='checkbox', _name='data_model_3D'), '3D Model', '',
                    INPUT(_type='checkbox', _name='data_model_interactions'), 'Interaction Model'),
             TR('', INPUT(_type='checkbox', _name='data_inferred'), 'Inferred', ''),
             TR(H5('Category: System')),
             TR('', INPUT(_type='checkbox', _name='system_organelles'), 'Organelles', '',
                    INPUT(_type='checkbox', _name='system_nucleus'), 'Nucleus', '',
                    INPUT(_type='checkbox', _name='system_cytoplasm'), 'Cytoplasm'),
             TR('', INPUT(_type='checkbox', _name='system_mitochondria'), 'Mitochondria', '',
                    INPUT(_type='checkbox', _name='system_chloroplast'), 'Chloroplast', '',
                    INPUT(_type='checkbox', _name='system_ribosome'), 'Ribosome'),
             TR('', INPUT(_type='checkbox', _name='system_extracellular'), 'Extracellular', '',
                    INPUT(_type='checkbox', _name='system_whole_cell'), 'Whole Cell', '',
                    INPUT(_type='checkbox', _name='system_tissues'), 'Tissues'),
             TR('', INPUT(_type='checkbox', _name='system_organs'), 'Organs', '',
                    INPUT(_type='checkbox', _name='system_organ_systems'), 'Organ Systems', '',
                    INPUT(_type='checkbox', _name='system_organism'), 'Organism'),
             TR('', INPUT(_type='checkbox', _name='system_population'), 'Population', ''),
             TR(H5('Category: Access')),
             TR('', INPUT(_type='checkbox', _name='access_web_forms_applications'), 'Web Forms', '',
                    INPUT(_type='checkbox', _name='access_programmatic'), 'Programmatic', '',
                    INPUT(_type='checkbox', _name='access_data_download'), 'Data Download'),
             TR('', INPUT(_type='checkbox', _name='access_submission'), 'Data Submission', ''),
             TR(H5('Category: Status')),
             TR('', INPUT(_type='checkbox', _name='status_alive'), 'Alive', '',
                    INPUT(_type='checkbox', _name='status_dead'), 'Dead', '',
                    INPUT(_type='checkbox', _name='status_unknown'), 'Unknown')]
    form = FORM(TABLE(table), INPUT(_type='submit', _name='submit'))
    if form.accepts(request.vars, session):

        redirect(URL(r=request, f='search_results'))
    return dict(form=form)


def search_results():
    return dict(results=session)


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to BioDBCat! Please login or register at the top right hand corner")
    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
