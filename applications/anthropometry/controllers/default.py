import math

def index():
    form = FORM(TABLE(
                TR(B('''Gender (required):'''), SELECT(['Male', 'Female'], _name='gender')),
                TR(B('''Age (required):'''), INPUT(_type='text', _name='age', _size=10), 
                   'years'),
                TR(B('''Height (required):'''), INPUT(_type='text', _name='height', _size=10), 
                   'centimetres'),
                TR(B('''Weight (required):'''), INPUT(_type='text', _name='weight', _size=10), 
                   'kilograms'),
                TR('Neck Circumference:', INPUT(_type='text', _name='neck', _size=10), 
                   'centimetres'),
                TR('Forearm Circumference:', INPUT(_type='text', _name='forearm', _size=10), 
                   'centimetres'),
                TR('Wrist Circumference:', INPUT(_type='text', _name='wrist', _size=10), 
                   'centimetres'),
                TR('Waist Circumference:', INPUT(_type='text', _name='waist', _size=10),
                   'centimetres'),
                TR('Hip Circumference:', INPUT(_type='text', _name='hip', _size=10), 
                   'centimetres'),
                TR('Thigh Circumference:', INPUT(_type='text', _name='thigh', _size=10), 
                   'centimetres'),
                TR('Calf Circumference:', INPUT(_type='text', _name='calf', _size=10), 
                   'centimetres'),
                TR('Chest Fold:', INPUT(_type='text', _name='chest', _size=10), 
                   'millimetres (skin fold: diagonal pinch between nipple and armpit)'),
                TR('Abdominal Fold:', INPUT(_type='text', _name='abdominal', _size=10), 
                   'millimetres (skin fold: vertical pinch, 1 inch beside navel)'),
                TR('Thigh Fold:', INPUT(_type='text', _name='thigh_fold', _size=10), 
                   'millimetres (skin fold: vertical pinch, middle of thigh)'),
                TR('Tricep Fold:', INPUT(_type='text', _name='tricep', _size=10), 
                   'millimetres (skin fold: vertical pinch, midway between shoulder and elbow)'),
                TR('Suprailiac Fold:', INPUT(_type='text', _name='suprailiac', _size=10), 
                   'millimetres (skin fold: diagonal pinch, directly above iliac crest)'),
                TR('', INPUT(_type='submit', _name='submit'))))
    form.vars.age = 36
    form.vars.height = 173
    form.vars.weight = 79.5
    form.vars.neck = 41
    form.vars.forearm = 26.5
    form.vars.wrist = 17
    form.vars.waist = 91.5
    form.vars.hip = 96.5
    form.vars.thigh = 57
    form.vars.calf = 40
    form.vars.chest = 20
    form.vars.abdominal = 18
    form.vars.thigh_fold = 15
    form.vars.tricep = 13
    form.vars.suprailiac = 20
    if form.accepts(request.vars, session):
        session.gender = form.vars.gender
        
        try: session.age = float(form.vars.age)
        except: session.age = 0
        
        try: session.height = float(form.vars.height)
        except: session.height = 0
        
        try: session.weight = float(form.vars.weight)
        except: session.weight = 0
        
        try:
            measurement = form.vars.neck.split(',')
            session.neck = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.neck = 0
        
        try:
            measurement = form.vars.forearm.split(',')
            session.forearm = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.forearm = 0
        
        try:
            measurement = form.vars.wrist.split(',')
            session.wrist = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.wrist = 0
        
        try:
            measurement = form.vars.waist.split(',')
            session.waist = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.waist = 0
        
        try:
            measurement = form.vars.hip.split(',')
            session.hip = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.hip = 0
        
        try:
            measurement = form.vars.thigh.split(',')
            session.thigh = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.thigh = 0
        
        try:
            measurement = form.vars.calf.split(',')
            session.calf = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: session.calf = 0
        
        try: 
            measurement = form.vars.chest.split(',')
            session.chest = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.chest = 0
        
        try:
            measurement = form.vars.abdominal.split(',')
            session.abdominal = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.abdominal = 0
        
        try:
            measurement = form.vars.thigh_fold.split(',')
            session.thigh_fold = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.thigh_fold = 0
        
        try: 
            measurement = form.vars.tricep.split(',')
            session.tricep = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.tricep = 0
        
        try:
            measurement = form.vars.suprailiac.split(',')
            session.suprailiac = sum([float(x.strip()) for x in measurement]) / len(measurement)
        except: 
            session.suprailiac = 0
        
        session.method = []
        calculate_anthropometry()
        redirect(URL(r=request, f='anthropometry_output'))
    return dict(form=form)

def anthropometry_output():
    return dict(results=session)

def USNavy_BF(gender):
    if gender == 'Male':
        d = 1.0324 - \
            0.19077*math.log10(session.waist - session.neck) + \
            0.15456*math.log10(session.height)
    if gender == 'Female':
        d = 1.29579 - \
            0.35004*math.log10(session.waist + session.hip - session.neck) + \
            0.22100*math.log10(session.height)
    r = (495 / d) - 450
    session.method.append('USNavy_BF')
    return round(r, 2)

def YMCA_BF(gender):
    weight = session.weight * 2.20462   # convert kg to pound
    waist = session.waist * 0.393701    # convert cm to inch
    if gender == 'Male':
        r = 100 * ((((4.15*waist) - (0.082*weight) - 98.42)) / weight)
    if gender == 'Female':
        r = 100 * ((((4.15*waist) - (0.082*weight) - 76.76)) / weight)
    session.method.append('YMCA_BF')
    return round(r, 2)

def mYMCA_BF(gender):
    weight = session.weight * 2.20462   # convert kg to pound
    waist = session.waist * 0.393701    # convert cm to inch
    if gender == 'Male':
        r = 100 * ((((4.15*waist) - (0.082*weight) - 94.42)) / weight)
    if gender == 'Female':
        wrist = session.wrist * 0.393701    # convert cm to inch
        hip = session.hip * 0.393701    # convert cm to inch
        forearm = session.forearm * 0.393701    # convert cm to inch
        r = 100 * ((((0.268*weight) - \
                    (0.318*wrist) + \
                    (0.157*waist) + \
                    (0.245*hip) - \
                    (0.434*forearm) - \
                    8.987)) / \
                weight)
    session.method.append('mYMCA_BF')
    return round(r, 2)

def CovertBailey_BF(gender):
    wrist = session.wrist * 0.393701    # convert cm to inch
    hip = session.hip * 0.393701    # convert cm to inch
    if gender == 'Male':
        waist = session.waist * 0.393701    # convert cm to inch
        forearm = session.forearm * 0.393701    # convert cm to inch
        if session.age < 30.01:
            r = waist + (0.5*hip) - (3.0*forearm) - wrist
        if session.age > 30:
            r = waist + (0.5*hip) - (2.7*forearm) - wrist
    if gender == 'Female':
        thigh = session.thigh * 0.393701    # convert cm to inch
        calf = session.calf * 0.393701    # convert cm to inch
        if session.age < 30.01:
            r = hip + (0.8*thigh) - (2.0*calf) - wrist
        if session.age > 30:
            r = hip + thigh - (2.0*calf) - wrist
    session.method.append('CovertBailey_BF')
    return round(r, 2)

def PenroseNelsonFisher_BF(gender):
    weight = session.weight * 2.20462   # convert kg to pound
    waist = session.waist * 0.393701    # convert cm to inch
    height = session.height * 0.393701  # convert cm to inch
    wrist = session.wrist * 0.393701    # convert cm to inch
    r = (100 * (weight - \
                (38.14 + \
                 (0.8995*weight) - \
                 (0.6135*session.age) - \
                 (0.005889*session.age*session.age) + \
                 (0.9978*height) - \
                 (3.807*(waist-wrist))))) / \
        weight
    session.method.append('PenroseNelsonFisher_BF')
    return round(r, 2)

def Siri(density):
    bf = (495 / float(density)) - 450
    return bf

def MifflinStJeorBMR(gender):
    if gender == 'Male':
        r = (10 * session.weight) + \
            (6.25 * session.height) - \
            (5 * session.age) + 5
    if gender == 'Female':
        r = (10 * session.weight) + \
            (6.25 * session.height) - \
            (5 * session.age) - 161
    session.method.append('MifflinStJeorBMR')
    return round(r, 2)

def HarrisBenedictBMR(gender):
    if gender == 'Male':
        r = 66.5 + \
            (13.75*session.weight) + \
            (5.003*session.height) - \
            (6.755*session.age)
    if gender == 'Female':
        r = 655.1 + \
            (9.563*session.weight) + \
            (1.850*session.height) - \
            (4.676*session.age)
    session.method.append('HarrisBenedictBMR')
    return round(r, 2)

def KleiberBMR(gender):
    r = 70 * (session.weight ** 0.75)
    session.method.append('KleiberBMR')
    return round(r, 2)

def RozaShizgalBMR(gender):
    if gender == 'Male':
        r = 88.362 + \
            (13.397*session.weight) + \
            (4.799*session.height) - \
            (5.677*session.age)
    if gender == 'Female':
        r = 447.593 + \
            (9.247*session.weight) + \
            (3.098*session.height) - \
            (4.330*session.age)
    session.method.append('RozaShizgalBMR')
    return round(r, 2)

def BMI(gender):
    height = session.height / 100
    r = session.weight / (height * height)
    session.method.append('BMI')
    return round(r, 2)

def Ponderal(gender):
    height = session.height / 100
    r = session.weight / (height * height * height)
    session.method.append('Ponderal')
    return round(r, 2)

def BFfromBMI(gender):
    if gender == 'Male': sex = 1
    if gender == 'Female': sex = 0
    r = (1.20 * session.BMI) + \
        (0.23 * session.age) - \
        (10.8 * sex) - 5.4
    session.method.append('BFfromBMI')
    return round(r, 2)

def Robinson_LW(gender):
    height = session.height * 0.393701  # convert cm to inch
    height = height - 60
    if gender == 'Male':
        r = 52.0 + (1.9*height)
    if gender == 'Female':
        r = 49.0 + (1.7*height)
    session.method.append('Robinson_LW')
    return round(r, 2)

def Miller_LW(gender):
    height = session.height * 0.393701  # convert cm to inch
    height = height - 60
    if gender == 'Male':
        r = 56.2 + (1.41*height)
    if gender == 'Female':
        r = 53.1 + (1.36*height)
    session.method.append('Miller_LW')
    return round(r, 2)

def Hamwi_LW(gender):
    height = session.height * 0.393701  # convert cm to inch
    height = height - 60
    if gender == 'Male':
        r = 48.0 + (2.7*height)
    if gender == 'Female':
        r = 45.5 + (2.2*height)
    session.method.append('Hamwi_LW')
    return round(r, 2)

def Devine_LW(gender):
    height = session.height * 0.393701  # convert cm to inch
    height = height - 60
    if gender == 'Male':
        r = 50.0 + (2.3*height)
    if gender == 'Female':
        r = 45.5 + (2.3*height)
    session.method.append('Devine_LW')
    return round(r, 2)

def BMI_LW(gender):
    lower = 18.5 * (session.height/100) * (session.height/100)
    upper = 25.0 * (session.height/100) * (session.height/100)
    session.method.append('BMI_LW')
    return (round(lower, 2), round(upper, 2))

def Pollock3(gender):
    fold = session.chest + session.abdominal + session.thigh_fold
    if gender == 'Male':
        density = 1.10938 - \
                  (0.0008267 * fold) + \
                  (0.0000016 * fold * fold) - \
                  (0.0002574 * session.age)
    if gender == 'Female':
        density = 1.0994921 - \
                  (0.0009929 * fold) + \
                  (0.0000023 * fold * fold) - \
                  (0.0001392 * session.age)
    r = Siri(density)
    session.method.append('Pollock3')
    return round(r, 2)

def Pollock3G(gender):
    if gender == 'Male':
        fold = session.chest + session.abdominal + session.thigh_fold
        density = 1.099075 - \
                  (0.0008290 * fold) + \
                  (0.0000026 * fold * fold) - \
                  (0.0002017 * session.age) - \
                  (0.00005675 * session.waist) + \
                  (0.00018586 * session.forearm)
    if gender == 'Female':
        fold = session.tricep + session.suprailiac + session.thigh_fold
        density = 1.1470292 - \
                  (0.0009376 * fold) + \
                  (0.000003 * fold * fold) - \
                  (0.0001392 * session.age) + \
                  (0.0005839 * session.hip)
    r = Siri(density)
    session.method.append('Pollock3G')
    return round(r, 2)

def Pollock4(gender):
    fold = session.abdominal + session.tricep + \
           session.thigh_fold + session.suprailiac
    if gender == 'Male':
        bodyfat = (0.29288 * fold) - \
                  (0.0005 * fold * fold) + \
                  (0.15845 * session.age) - \
                  5.76377
    if gender == 'Female':
        bodyfat = (0.41563 * fold) - \
                  (0.00112 * fold * fold) + \
                  (0.03661 * session.age) - \
                  4.03653
    session.method.append('Pollock4')
    return round(bodyfat, 2)

def BehnkeWilmore_S(gender):
    LBW = (0.7927 * session.weight) - \
          (0.3676 * session.abdominal) + \
          10.260
    FBW = session.weight - LBW
    bodyfat = (FBW * 100)/session.weight
    session.method.append('BehnkeWilmore_S')
    return round(bodyfat, 2)

def BehnkeWilmore_C(gender):
    LBW = (1.0817 * session.weight) - \
          (0.7396 * session.waist) + \
          44.636
    FBW = session.weight - LBW
    bodyfat = (FBW * 100)/session.weight
    session.method.append('BehnkeWilmore_C')
    return round(bodyfat, 2)

def calc(gender):
    if gender == 'Male':
        pass
    if gender == 'Female':
        pass
    r = 0
    session.method.append('r')
    return round(r, 2)

def calculate_male_anthropometry():
    if (session.height > 0 and \
        session.neck > 0 and \
        session.waist > 0):
        session.USNavy_BF = USNavy_BF('Male')
    if (session.weight > 0 and \
        session.waist > 0):
        session.YMCA_BF = YMCA_BF('Male')
    if (session.weight > 0 and \
        session.waist > 0):
        session.mYMCA_BF = mYMCA_BF('Male')
    if (session.wrist > 0 and \
        session.hip > 0 and \
        session.waist > 0 and \
        session.forearm > 0):
        session.CovertBailey_BF = CovertBailey_BF('Male')
    if (session.age > 0 and \
        session.height > 0 and \
        session.weight > 0 and \
        session.wrist > 0 and \
        session.waist > 0):
        session.PenroseNelsonFisher_BF = PenroseNelsonFisher_BF('Male')
    if (session.weight > 0 and \
        session.waist > 0):
        session.BehnkeWilmore_C = BehnkeWilmore_C('Male')
    if (session.height > 0 and \
        session.weight > 0 and \
        session.age > 0):
        session.MifflinStJeorBMR = MifflinStJeorBMR('Male')
        session.HarrisBenedictBMR = HarrisBenedictBMR('Male')
        session.RozaShizgalBMR = RozaShizgalBMR('Male')
    if (session.height > 0 and \
        session.weight > 0):
        session.BMI = BMI('Male')
        session.Ponderal = Ponderal('Male')
    if (session.height > 0 and \
        session.weight > 0 and \
        'BMI' in session.method):
        session.BFfromBMI = BFfromBMI('Male')
    if (session.height > 0):
        session.Robinson_LW = Robinson_LW('Male')
        session.Miller_LW = Miller_LW('Male')
        session.Hamwi_LW = Hamwi_LW('Male')
        session.Devine_LW = Devine_LW('Male')
        session.BMI_LW = BMI_LW('Male')
    if (session.weight > 0):
        session.KleiberBMR = KleiberBMR('Male')
    if (session.age > 0 and \
        session.chest > 0 and \
        session.abdominal > 0 and \
        session.thigh_fold > 0):
        session.Pollock3 = Pollock3('Male')
    if (session.age > 0 and \
        session.chest > 0 and \
        session.abdominal > 0 and \
        session.thigh_fold > 0 and \
        session.waist > 0 and \
        session.forearm > 0):
        session.Pollock3G = Pollock3G('Male')
    if (session.age > 0 and \
        session.abdominal > 0 and \
        session.tricep > 0 and \
        session.suprailiac > 0 and \
        session.thigh_fold > 0):
        session.Pollock4 = Pollock4('Male')
    if (session.weight > 0 and \
        session.abdominal > 0):
        session.BehnkeWilmore_S = BehnkeWilmore_S('Male')

def calculate_female_anthropometry():
    if (session.height > 0 and \
        session.neck > 0 and \
        session.waist > 0 and \
        session.hip > 0):
        session.USNavy_BF = USNavy_BF('Female')
    if (session.weight > 0 and \
        session.waist > 0):
        session.YMCA_BF = YMCA_BF('Female')
    if (session.weight > 0 and \
        session.waist > 0 and \
        session.hip > 0 and \
        session.forearm > 0 and \
        session.wrist > 0):
        session.mYMCA_BF = mYMCA_BF('Female')
    if (session.wrist > 0 and \
        session.hip > 0 and \
        session.thigh > 0 and \
        session.calf > 0):
        session.CovertBailey_BF = CovertBailey_BF('Female')
    if (session.weight > 0 and \
        session.waist > 0):
        session.BehnkeWilmore_C = BehnkeWilmore_C('Female')
    if (session.height > 0 and \
        session.weight > 0 and \
        session.age > 0):
        session.MifflinStJeorBMR = MifflinStJeorBMR('Female')
        session.HarrisBenedictBMR = HarrisBenedictBMR('Female')
        session.RozaShizgalBMR = RozaShizgalBMR('Female')
    if (session.height > 0 and \
        session.weight > 0):
        session.BMI = BMI('Female')
        session.Ponderal = Ponderal('Female')
    if (session.height > 0 and \
        session.weight > 0 and \
        'BMI' in session.method):
        session.BFfromBMI = BFfromBMI('Female')
    if (session.height > 0):
        session.Robinson_LW = Robinson_LW('Female')
        session.Miller_LW = Miller_LW('Female')
        session.Hamwi_LW = Hamwi_LW('Female')
        session.Devine_LW = Devine_LW('Female')
        session.BMI_LW = BMI_LW('Female')
    if (session.weight > 0):
        session.KleiberBMR = KleiberBMR('Male')
    if (session.age > 0 and \
        session.chest > 0 and \
        session.abdominal > 0 and \
        session.thigh_fold > 0):
        session.Pollock3 = Pollock3('Female')
    if (session.age > 0 and \
        session.tricep > 0 and \
        session.suprailiac > 0 and \
        session.thigh_fold > 0 and \
        session.hip > 0):
        session.Pollock3G = Pollock3G('Female')
    if (session.age > 0 and \
        session.abdominal > 0 and \
        session.tricep > 0 and \
        session.suprailiac > 0 and \
        session.thigh_fold > 0):
        session.Pollock4 = Pollock4('Female')
    if (session.weight > 0 and \
        session.abdominal > 0):
        session.BehnkeWilmore_S = BehnkeWilmore_S('Female')

def body_composition():
    skinfolds = [session.Pollock3, 
                 session.Pollock3G, 
                 session.Pollock4,
                 session.BehnkeWilmore_S]
    session.skinfold_bf = sum(skinfolds) / len(skinfolds)
    session.sf_fat_mass = session.weight * (session.skinfold_bf/100)
    session.sf_lean_mass = session.weight - session.sf_fat_mass
    session.method.append('skinfold_bf')
    
def calculate_anthropometry():
    if session.gender == 'Male':
        calculate_male_anthropometry()
        body_composition()
    elif session.gender == 'Female':
        calculate_female_anthropometry()
        body_composition()
