ENSEMBLES = (
    ('storm', 'State Storm'),
    ('varsity', "ISUCF'V'MB"),
)

INSTRUMENTS = (
    ('Alto Sax', 'Alto Sax'),
    ('Baritone', 'Baritone'),
    ('Bass Drum', 'Bass Drum'),
    ('Bass Trombone', 'Bass Trombone'),
    ('Clarinet', 'Clarinet'),
    ('Color Guard', 'Color Guard'),
    ('Feature Twirler', 'Feature Twirler'),
    ('Melophone', 'Melophone'),
    ('Piccolo', 'Piccolo'),
    ('Snare Drum', 'Snare Drum'),
    ('Sousaphone', 'Sousaphone'),
    ('Tenor Drums', 'Tenor Drums'),
    ('Tenor Sax', 'Tenor Sax'),
    ('Trombone 1', 'Trombone 1'),
    ('Trombone 2', 'Trombone 2'),
    ('Trumpet 1', 'Trumpet 1'),
    ('Trumpet 2', 'Trumpet 2'),
    ('Trumpet 3', 'Trumpet 3'),
)

MEALS = (
    ('Standard', 'Standard'),
    ('Vegitarian', 'Vegitarian'),
    ('Gluten Free', 'Gluten Free (Please provide medical documentation)'),
    ('Self Provided', 'Will Provide Own'),
)

YEARS = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5+', '5+'),
)

GENDERS = (
    ('Female', 'Female'),
    ('Male', 'Male'),
)

def shoe_size_gen(start, stop, step=.5):
    while start <= stop:
        yield start
        start += step

SHOE_SIZES = tuple((str(i),str(i)) for i in shoe_size_gen(4, 14, .5))

TSHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
)

