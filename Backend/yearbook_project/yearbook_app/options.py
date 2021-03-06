DEGREES     = [(u'FYBS', u'Four Year BS'), (u'BTECH', u'Bachelor of Technology'), (u'MTECH', u'Master of Technology'), (u'DD', u'B.Tech. + M.Tech. Dual Degree'), (u'MSC', u'Master of Science'), (u'PHD', u'Doctor of Philosophy'), (u'BDES', u'Bachelor of Design'), (u'MDES', u'Master of Design'), (u'MPHIL', u'Master of Philosophy'), (u'MMG', u'Master of Management'), (u'MSEx', u'M.S. (Exit Degree)'), (u'MtechEx', u'Master of Technology (Exit Degree)'), (u'MtechPhDDD', u'M.Tech. + Ph.D. Dual Degree'), (u'PC', u'Preparatory Course'), (u'VS', u'Visiting Student'), (u'MPhilEx', u'Master of Philosophy (Exit Degree)'), (u'MScEx', u'Master of Science (Exit Degree)'), (u'MScMTechDD', u'M.Sc. + M.Tech. Dual Degree'), (u'MScPhDDD', u'M.Sc. + Ph.D. Dual Degree'), (u'MPhilPhDDD', u'M.Phil. + Ph.D. Dual Degree'), (u'EMBA', u'Executive MBA'), (u'IMTECH', u'Integrated M.Tech.'), (u'MSCBR', u'Master of Science By Research'), (u'TYMSC', u'Two Year M.Sc.'), (u'FYIMSC', u'Five Year Integrated M.Sc.'), (u'DIIT', u'D.I.I.T.'), (u'DIITEx', u'D.I.T.T. (Exit Degree)')]


DEGREES_MOD = [(u'FYBS', u'Four Year BS'), (u'BTech', u'Bachelor of Technology'), (u'MTech', u'Master of Technology'), (u'DD', u'B.Tech. + M.Tech. Dual Degree'), (u'MSc', u'Master of Science'), (u'PhD', u'Doctor of Philosophy'), (u'BDes', u'Bachelor of Design'), (u'MDes', u'Master of Design'), (u'M.Phil', u'Master of Philosophy'), (u'MMG', u'Master of Management'), (u'MSEx', u'M.S. (Exit Degree)'), (u'MTechEx', u'Master of Technology (Exit Degree)'), (u'MTechPhDDD', u'M.Tech. + Ph.D. Dual Degree'), (u'PC', u'Preparatory Course'), (u'VS', u'Visiting Student'), (u'MPhilEx', u'Master of Philosophy (Exit Degree)'), (u'MScEx', u'Master of Science (Exit Degree)'), (u'MScMTechDD', u'M.Sc. + M.Tech. Dual Degree'), (u'MScPhDDD', u'M.Sc. + Ph.D. Dual Degree'), (u'MPhilPhDDD', u'M.Phil. + Ph.D. Dual Degree'), (u'EMBA', u'Executive MBA'), (u'IMTech', u'Integrated M.Tech.'), (u'MScBR', u'Master of Science By Research'), (u'TYMSc', u'Two Year M.Sc.'), (u'FYIMSc', u'Five Year Integrated M.Sc.'), (u'DIIT', u'D.I.I.T.'), (u'DIITEx', u'D.I.T.T. (Exit Degree)')]

NOTIFICATION_PREFERENCES = (
	(0, u"Do not send any notifications"),
	(1, u"Send Only if someone writes on my wall"),
	(2, u"In addition to above, Send if I'm tagged in a post"),
	(3, u"In addition to above, Send if someone tags me in a Impression"),
	(4, u"Send Everytime someone tags me or writes for me or comments on my post"),
)

DEPARTMENTS = {
	u'Aerospace Engineering': 'Aerospace Engg', 
	u'Animation': 'Animation', 
	u'Application Software Centre': 'ASC', 
	u'Applied Geophysics': 'Applied Geophysics', 
	u'Applied Statistics and Informatics': 'ASI', 
	u'Biomedical Engineering': 'Biomedical Engg', 
	u'Biosciences and Bioengineering': 'Biosciences & BioEngg', 
	u'Biotechnology': 'Biotechnology', 
	u'Centre for Aerospace Systems Design and Engineering': 'CASDE', 
	u'Centre for Distance Engineering Education Programme': 'CDEEP', 
	u'Centre for Environmental Science and Engineering': 'CESE', 
	u'Centre for Formal Design and Verification of Software': 'CFDVS', 
	u'Centre for Research in Nanotechnology and Science': 'CRNS', 
	u'Centre for Technology Alternatives for Rural Areas': 'CTARA', 
	u'Centre for Urban Science and Engineering': 'CUSE', 
	u'Centre of Studies in Resources Engineering': 'CSRE', 
	u'Chemical Engineering': 'Chemical Engg', 
	u'Chemistry': 'Chemistry', 
	u'Civil Engineering': 'Civil Engg', 
	u'Climate Studies': 'Climate Studies', 
	u'Computer Centre': 'CC', 
	u'Computer Science & Engineering': 'CSE', 
	u'Continuing Education Programme': 'CEP', 
	u'Corrosion Science and Engineering': 'Corrosion Science & Engg', 
	u'Desai Sethi Centre for Entrepreneurship': 'DSCE', 
	u'Earth Sciences': 'Earth Sciences', 
	u'Educational Technology': 'Educational Technology', 
	u'Electrical Engineering': 'EE', 
	u'Energy Science and Engineering': 'Energy Science and Engg', 
	u'Economics (HSS)': 'Economics',
	u'Engineering Physics': 'Engineering Physics', 
	u'Humanities & Social Science': 'HSS', 
	u'IITB-Monash Research Academy': 'IITB-Monash', 
	u'Industrial Design Centre': 'IDC', 
	u'Industrial Engineering and Operations Research': 'IEOR', 
	u'Industrial Management': 'Industrial Management', 
	u'Interaction Design': 'Interaction Design', 
	u'Kanwal Rekhi School of Information Technology': 'KRSIT', 
	u'Material Science': 'Material Science', 
	u'Materials, Manufacturing and Modelling': 'Materials, Manufacturing and Modelling', 
	u'Mathematics': 'Mathematics', 
	u'Mechanical Engineering': 'Mechanical Engg', 
	u'Metallurgical Engineering & Materials Science': 'MEMS', 
	u'Mobility and Vehicle Design': 'Mobility and Vehicle Design', 
	u'National Centre for Aerospace Innovation and Research': 'NCAIR', 
	u'National Centre for Mathematics': 'NCM', 
	u'Physical Education': 'Physical Education', 
	u'Physics': 'Physics', 
	u'Physics, Material Science': 'Physics, Material Science', 
	u'Preparatory Course': 'Preparatory Course', 
	u'Reliability Engineering': 'Reliability Engineering', 
	u'Shailesh J. Mehta School of Management': 'SJM-SOM', 
	u'Sophisticated Analytical Instrument Facility': 'Sophisticated Analytical Instrument Facility', 
	u'Systems and Control Engineering': 'SysCon Engg', 
	u'Tata Center for Technology and Design': 'Tata Center', 
	u'Technology and Development': 'Tech and Dev', 
	u'Visual Communication': 'Visual Communication', 
	u'Wadhwani Research Centre for Bioengineering': 'Wadhwani Research Centre', 
	u'Centre for Policy Studies': 'Centre for Policy Studies'
}
ACTIVITIES = list(set([
	'Mood Indigo', 'Techfest', 'E-Cell', 'Insight', 'Abhyuday', 
	'SARC', 'InSync', 'Fourthwall', 'Silverscreen', 'Roots', 
	'Rang', 'Pixels', 'WeSpeak', 'Lit Club', 'Litzkrieg', 'Music Club', 
	'Saaz','Design Club', 'Staccato', 'Vaani', 'Athletics', 'Aquatics', 
	'Basketball', 'Board Games', 'Cricket', 'Football', 'Kho-Kho', 'Lawn Tennis', 
	'Table Tennis', 'Weightlifting', 'Hockey', 'Squash', 'Badminton', 'Volleyball', 
	'STAB', 'Robotics Club', 'Electronics Club', 'Maths and Physics Club', 
	'Web and Coding Club', 'Aeromodelling Club', 'Astronomy Club', 'Finance Club', 
	'Analytics Club', 'Consult Club', 'ShARE', 'IITB Student Satellite Program', 
	'IITB Racing', 'AUV', 'Saathi','Institute Sports Council', 
	'Innovation Cell', 'Team Shunya', 'Mars Society India', 'Academic Council', 
	'Hostel Council', 'Adventure Club','Tinkerers Lab','NSS','Department Council',
	'Institute Cultural Council', 'Institute Technical Council','AZeotropy', 'Radiance',
	'Aakaar','PT Cell','LifeStyle Club','BioTech Club','GRA','SMP','ISCP', 'Sustainability Cell IITB', 'Rakshak IITB'
]))
null=None
ACTIVITIES2=[
	(null,'None'),
	('AUV','AUV'),
	('AZeotropy','AZeotropy'),
	('Aakaar','Aakaar'),
	('Aavhaan', 'Aavhaan'),
	('Abhyuday','Abhyuday'),
	('Academic Council','Academic Council'),
	('Adventure Club','Adventure Club'),
	('Aeromodelling Club','Aeromodelling Club'),
	('Analytics Club','Analytics Club'),
	('Aquatics','Aquatics'),
	('Astronomy Club','Astronomy Club'),
	('Athletics','Athletics'),
	('Badminton','Badminton'),
	('Basketball','Basketball'),
	('BioTech Club','BioTech Club'),
	('Board Games','Board Games'),
	('Chess', 'Chess'),
	('Consult Club','Consult Club'),
	('Comedy Club','Comedy Club'),
	('Cricket','Cricket'),
	# ('Culinary Club','Culinary Club'),
	('Department Council','Department Council'),
	('Design Club','Design Club'),
	('E-Cell','E-Cell'),
	('Electronics and Robotics Club','Electronics and Robotics Club'),
	('Finance Club','Finance Club'),
	('Football','Football'),
	('Fourthwall','Fourthwall'),
	('GRA','GRA'),
	('Hockey','Hockey'),
	('Hostel Affairs Council','Hostel Affairs Council'),
	('Hostel Council','Hostel Council'),
	# ('Hult Prize Competition','Hult Prize Competition'),
	('IITB Racing','IITB Racing'),
	('IITB Student Satellite Program','IITB Student Satellite Program'),
	('ISCP','ISCP'),
	('InSync','InSync'),
	('Innovation Cell','Innovation Cell'),
	('Insight','Insight'),
	('Institute Cultural Council','Institute Cultural Council'),
	('Institute Sports Council','Institute Sports Council'),
	('Institute Technical Council','Institute Technical Council'),
	('Kho-Kho','Kho-Kho'),
	('Lawn Tennis','Lawn Tennis'),
	('LifeStyle Club','LifeStyle Club'),
	('Lit Club','Lit Club'),
	('Litzkrieg','Litzkrieg'),
	('Mars Society India','Mars Society India'),
	('Maths and Physics Club','Maths and Physics Club'),
	('Mood Indigo','Mood Indigo'),
	('Music Club','Music Club'),
	('NCC','NCC'),
	('NSS','NSS'),
	('PT Cell','PT Cell'),
	('Pixels','Pixels'),
	('Radiance','Radiance'),
	('Rang','Rang'),
	# ('Robotics Club','Robotics Club'),
	('Roots','Roots'),
	('SARC','SARC'),
	('SMP','SMP'),
	('STAB','STAB'),
	('Saathi','Saathi'),
	('Saaz','Saaz'),
	('ShARE','ShARE'),
	('Silverscreen','Silverscreen'),
	('Squash','Squash'),
	('Staccato','Staccato'),
	('Table Tennis','Table Tennis'),
	('Team Shunya','Team Shunya'),
	('Techfest','Techfest'),
	('Tinkerers Lab','Tinkerers Lab'),
	('Vaani','Vaani'),
	('Volleyball','Volleyball'),
	('WeSpeak','WeSpeak'),
	('Web and Coding Club','Web and Coding Club'),
	('Weightlifting','Weightlifting'),
	('Sustainability Cell IITB', 'Sustainability Cell IITB'),
	('Rakshak IITB', 'Rakshak IITB'),
]

QUESTIONS = [
	('pastself', 'If you get the chance to meet freshie self again, what is that one thing you will tell him or her?'),
	('movie', "You become famous and someone wants to film a movie on your college life, what will it be called?"),
	('neverever',"In my insti life, Never have I Ever:"),
	('memories',"If you could pack up a bunch of things from the institute to keep with you forever, what will those be?")
]

