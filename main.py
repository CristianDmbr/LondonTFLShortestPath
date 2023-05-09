graph = {
    # Bakerloo
    "Harrow & Wealdstone": {"Kenton": 2},
    "Kenton": {"South Kenton": 2, "Harrow & Wealdstone": 2},
    "South Kenton": {"North Wembley": 2, "Kenton": 2},
    "North Wembley": {"Wembley Central": 2, "South Kenton": 2},
    "Wembley Central": {"Stonebridge Park": 2, "North Wembley": 2},
    "Stonebridge Park": {"Harlesden" : 2,"Wembley Central": 2},
    "Harlesden": {"Willesden Junction": 2, "Stonebridge Park": 2},
    "Willesden Junction" : {"Harlesden" : 2,"Kensal Green": 3},
    "Kensal Green" : {"Queen's Park" : 2, "Willesden Junction": 3},
    "Queen's Park" : {"Kensal Green" : 2, "Kilburn Park": 2},
    "Kilburn Park" : {"Maida Vale" : 2, "Queen's Park" : 2},
    "Maida Vale" : {"Kilburn Park" : 2,"Warwick Avenue" :1},
    "Warwick Avenue" : {'Maida Vale' : 1, "Paddington" : 2},
    "Paddington" : {"Warwick Avenue" : 2,"Paddington - Circle" : 0,"Edgware Road" : 2,"Bayswater" : 2 },

    "Edgware Road" : {"Paddington" :2 ,"Marylebone" : 1,"Paddington - Circle" : 3},
    "Marylebone" : {"Baker Street" : 2, "Edgware Road" :1},
    "Baker Street" : {"Marylebone" : 2,"Regent's Park" : 2},
    "Regent's Park" : {"Baker Street" : 2,"Oxford Circus": 2},
    "Oxford Circus" : {"Regent's Park" : 2,"Piccadilly Circus": 2,"Bond Street" : 2, "Warren Street" :2, "Green Park" : 2},
    "Piccadilly Circus":{"Oxford Circus" : 2,"Charing Cross": 2, "Leicester Square" : 1, "Green Park" : 2},
    "Charing Cross" : {"Piccadilly Circus" : 2,"Embankment" :1, "Leicester Square" : 1},
    "Embankment" : {"Charing Cross": 1,"Waterloo" : 2,"Temple" : 2},
    "Waterloo" : {"Embankment" : 2,"Lambeth North" : 2 , "Kennington" : 3},
    "Lambeth North" : {'Waterloo' : 2, "Elephant & Castle" : 3},
    "Elephant & Castle" : {"Lambeth North" : 3, "Borough" : 2, "Kennington" :2},

    # Central
    "Epping": {"Theydon Bois": 3},
    "Theydon Bois": {"Epping": 3, "Debden": 3},
    "Debden": {"Theydon Bois": 3, "Loughton": 2},
    "Loughton": {"Debden": 2, "Buckhurst Hill": 3},
    "Buckhurst Hill": {"Loughton": 3, "Woodford": 2},
    "Woodford": {"Buckhurst Hill": 2,"South Woodford": 3, "Roding Valley" : 4},
    "South Woodford":{"Woodford": 3,"Snaresbrook":2},
    "Snaresbrook": {"South Woodford": 2 , "Leytonstone": 2},
    "Leytonstone": {"Snaresbrook": 2},
    "Roding Valley" : {"Woodford" : 4 , "Chigwell" : 3},
    "Chigwell" : {"Roding Valley" : 3, "Grange Hill" : 2},
    "Grange Hill" : {"Chigwell" : 2, "Hainault" : 5},
    "Hainault" : {'Grange Hill' : 5, "Fairlop" : 2},
    "Fairlop" : {"Hainault" : 2,"Barkingside" : 2},
    "Barkingside" : {'Fairlop' :2 , "Newbury Park" : 2 },
    "Newbury Park" : {"Barkingside" : 2,"Gants Hill" : 3},
    "Gants Hill" : {"Newbury Park" : 3, "Redbridge" : 2},
    "Redbridge" : {"Gants Hill" : 2,"Wanstead" : 2},
    "Wanstead" : {"Redbridge" : 2,"Leytonstone" : 2},
    "Leytonstone" : {"Wanstead" : 2,"Leyton" :2},
    "Leyton" : {"Leytonstone" :2,"Stratford" :3},
    "Stratford" : {"Leyton" : 3, "Mile End - Central" :4},
    "Mile End - Central" :{'Stratford' :4, "Bethnal Green" : 2, "Mile End - District" : 0},
    "Bethnal Green" : {"Mile End - Central" : 2, "Liverpool Street" : 3},
    "Liverpool Street" : {"Bethnal Green" : 3, "Bank" : 2,"Moorgate" : 2, "Aldgate East" : 3},
    "Bank" : {"Liverpool Street" :2,"St. Paul's" :2, "Moorgate" : 2 , "London Bridge" : 2, "Waterloo" : 5},
    "St. Paul's" : {"Bank" :2, "Chancery Lane" : 2},
    "Chancery Lane" :{"St. Paul's" : 2, "Holborn" : 1},
    "Holborn" : {"Chancery Lane" : 1,"Tottenham" :2, "Russell Square" : 2, "Covent Garden" : 2},
    "Tottenham" : {"Holborn" :2,"Oxford Circus" :1, "Goodge Street" : 1, "Leicester Square" : 2},
    "Bond Street" : {"Oxford Circus" : 2,"Marble Arch" :2, "Baker Street" : 3, "Green Park" : 2},
    "Marble Arch" : {"Bond Street" : 2, "Lancaster Gate" : 3},
    "Lancaster Gate" : {"Marble Arch" : 3,"Queensway" :2},
    "Queensway" : {"Lancaster Gate" : 2, "Notting Hill Gate" :2},
    "Notting Hill Gate" : {"Queensway" : 2, "Holland Park" : 1},
    "Holland Park" : {"Notting Hill Gate" :1,"Shepherd's Bush" : 2},
    "Shepherd's Bush" : {"Holland Park" : 2,"White City" : 3},
    "White City" : {"Shepherd's Bush": 3,"East Acton" : 3},
    "East Acton" : {"White City" : 3 , "North Acton" : 2},
    "North Acton" : {"East Acton" :2,"Hanger Lane" : 3 , "West Acton" : 2},
    "West Acton" : {"North Acton" :2,"Ealing Broadway" : 3},
    "Ealing Broadway" : {"West Acton" : 3, "Ealing Common" : 5},
    "Hanger Lane" :{"North Acton" : 3, "Perivale" : 3},
    "Perivale" : {"Hanger Lane" : 3, "Greenford" :2},
    "Greenford" : {"Perivale" : 2,"Northolt" :2},
    "Northolt" : {"Greenford" : 2, "South Ruislip" : 3},
    "South Ruislip" : {"Northolt": 3, "Ruislip Gardens" : 2},
    "Ruislip Gardens" :{"South Ruislip" :2,"West Ruislip" :2},
    "West Ruislip" : {"Ruislip Gardens" : 2},

    # Circle
    "Paddington - Circle" : {"Edgware Road" : 3 , "Bayswater" : 2, "Paddington" : 0, "Royal Oak" : 2},
    "Bayswater" : {"Paddington - Circle" : 2, "Notting Hill Gate" : 2},
    "Notting Hill Gate" : {"Bayswater": 2, "High Street Kensington" :2},
    "High Street Kensington" :{"Notting Hill Gate" : 2, "Gloucester Road" : 3, "Earl's Court" : 5},
    "Gloucester Road" : {"High Street Kensington" : 3, "South Kensington" : 3, "Earl's Court" : 2,},
    "South Kensington" : {"Gloucester Road" : 3, "Sloane Square" : 2, "Knightsbridge" : 2},
    "Sloane Square" : {"South Kensington" :2, "Victoria" : 2},
    "Victoria" : {"Sloane Square" : 2, "St. James's Park" :2, "Green Park" : 2 , "Pimlico" : 2},
    "St. James's Park" : {"Victoria" :2, "Westminster" :2},
    "Westminster" : {"St. James's Park" : 2, "Embankment" :1, "Green Park" : 2, "Waterloo" : 2},

    "Temple" : {"Embankment" : 2, "Blackfriars" :1},
    "Blackfriars" : {"Temple" :1, "Mansion House" :2},
    "Mansion House" : {"Blackfriars" : 2 , "Cannon Street" :2},
    "Cannon Street" : {"Mansion House":2, "Monument" :1},
    "Monument" : {"Cannon Street" :1, "Tower Hill": 2},
    "Tower Hill" : {"Monument" : 2, "Aldgate" :2},
    "Aldgate" : {"Tower Hill"  : 2, "Liverpool Street" : 3},
    "Moorgate" : {"Liverpool Street" :2, "Barbican" : 2, "Old Street" :2 , "Bank" :2},
    "Barbican" : {"Moorgate" : 2, "Farringdon" :1},
    "Farringdon" : {"Barbican" : 1, "King's Cross St. Pancras" :4},
    "King's Cross St. Pancras": {"Farringdon" : 4, "Euston Square" :2,"Euston" : 2 ,"Angel" : 3, "Caledonian Road" : 4, "Russell Square" : 2, "Highbury & Islington" : 2},
    "Euston Square":{"King's Cross St. Pancras":2, "Great Portland Street" :2},
    "Great Portland Street" : {"Euston Square" : 2, "Baker Street" :2},
    "Baker Street" : {"Great Portland Street" : 2, "Edgware Road" :3 , "St. John's Wood" : 3, "Bond Street" : 2, "Finchley Road" : 5},
    "Edgware Road" : {"Baker Street" : 3},
    "Royal Oak" : {"Paddington - Circle" : 2, "Westbourne Park" :2},
    "Westbourne Park" : {"Royal Oak" :2, "Ladbroke Grove" : 2},
    "Ladbroke Grove" : {"Westbourne Park" : 2 ,"Latimer Road": 2},
    "Latimer Road" : {"Ladbroke Grove" :2, "Wood Lane" :2},
    "Wood Lane" : {"Latimer Road" :2, "Shepherd's Bush Market" : 2},
    "Shepherd's Bush Market" : {"Wood Lane" : 2, "Goldhawk Road" :1},
    "Goldhawk Road" : {"Shepherd's Bush Market" : 1 , "Hammersmith" :2},
    "Hammersmith" : {"Goldhawk Road" :2, "Acton Town" : 8 , "Turnham Green" : 4},

    # District
    "Upminster" : {"Upminster Bridge" : 2},
    "Upminster Bridge" : {"Upminster" : 2, "Hornchurch" :2},
    "Hornchurch" : {"Upminster Bridge" :2, "Elm Park" :2},
    "Elm Park" : {"Hornchurch" :2, "Dagenham East" : 3},
    "Dagenham East" : {"Elm Park" : 3, "Dagenham Heathway" :2},
    "Dagenham Heathway" : {"Dagenham East" :2, "Becontree" :3},
    "Becontree" :{"Dagenham Heathway" : 3, "Upney" :2},
    "Upney" : {"Becontree": 2, "Barking" :3},
    "Barking" : {"Upney" : 3, "East Ham" : 4},
    "East Ham" : {"Barking" :4, "Upton Park" :2},
    "Upton Park" : {"East Ham" : 2, "Plaistow" :2},
    "Plaistow" : {'Upton Park' :2 , "West Ham" :2},
    "West Ham" : {"Plaistow" :2, "Bromley-by-Bow" :2 ,"Stratford" : 2,"Canning Town": 3},
    "Bromley-by-Bow" : {"West Ham" : 2, "Bow Road" :2},
    "Bow Road" : {"Bromley-by-Bow" : 2 , "Mile End - District" :2},
    "Mile End - District" : {"Bow Road" : 2, "Mile End - Central" : 0,"Stepney Green" : 2},
    "Stepney Green"  : {"Mile End - District" : 2 , "Whitechapel" : 3},
    "Whitechapel" : {"Stepney Green" : 3, "Aldgate East" : 2},
    "Aldgate East" : {"Whitechapel" : 2, "Tower Hill" : 3, "Liverpool Street" : 3},
    "Earl's Court" : {"Gloucester Road" : 2, "High Street Kensington" : 5, "West Kensington" : 2, "West Brompton" : 2, "Barons Court" : 3},
    "West Brompton" : {"Earl's Court" : 2, "Fulham Broadway" : 2},
    "Fulham Broadway" : {"West Brompton" :2, "Parsons Green" :2 },
    "Parsons Green" : {"Fulham Broadway" : 2, "Putney Bridge" : 3},
    "Putney Bridge" : {"Parsons Green" : 3, "East Putney" : 3},
    "East Putney" : {"Putney Bridge" : 3, "Southfields" : 2},
    "Southfields" : {"East Putney" :2 , "Wimbledon Park" : 2},
    "Wimbledon Park" : {"Southfields" : 2, "Wimbledon" : 4},
    "Wimbledon" : {"Wimbledon Park" :4},
    "West Kensington" : {"Earl's Court" :2, "Barons Court" : 2},
    "Barons Court" : {"West Kensington" : 2, "Hammersmith" : 3},
    "Hammersmith" : {'Barons Court' : 3,"Ravenscourt Park" : 2},
    "Ravenscourt Park" : {"Hammersmith" : 2, "Stamford Brook" : 2},
    "Stamford Brook" : {"Ravenscourt Park" :2, "Turnham Green" :1},
    "Turnham Green" : {"Stamford Brook" : 1, "Gunnersbury" : 3, "Chiswick Park" : 2, "Hammersmith" : 4, "Acton Town": 4},
    "Gunnersbury" : {"Turnham Green" : 3, "Kew Gardens" : 2},
    "Kew Gardens" : {"Gunnersbury" : 2, "Richmond" :4},
    "Richmond" : {"Kew Gardens" :4},
    "Chiswick Park" : {"Turnham Green" : 2, "Acton Town" :2},
    "Acton Town" : {"Chiswick Park" : 2,"Ealing Common" : 2, "Hammersmith" : 8, "Turnham Green" : 4, "South Ealing": 3},
    "Ealing Common" : {"Acton Town" :2,"Ealing Broadway" : 5, "North Ealing" : 2},
    "South Ealing" : {"Acton Town" : 3, "Northfields" : 1},
    "Northfields" : {"South Ealing" : 1, "Boston Manor" : 2},
    "Boston Manor" : {"Northfields" : 2, "Osterley" : 3},


    # Hammersmith & City
    # Just adjusted some previous nodes

    # Jubilee
    "Stanmore" : {"Canons Park" : 4},
    "Canons Park" : {"Stanmore" : 4, "Queensbury" : 3},
    "Queensbury" : {"Canons Park" : 3, "Kingsbury" :2},
    "Kingsbury" : {"Queensbury" :2, "Wembley Park" : 3},
    # Part of Metropolitan
    "Wembley Park" : {"Kingsbury" :3 , "Neasden" : 4, "Preston Road" : 3,"Finchley Road" : 7},
    "Neasden" : {"Wembley Park" : 4 , "Dollis Hill" : 2},
    "Dollis Hill" : {"Neasden" : 2, "Willesden Green" : 2},
    "Willesden Green" : {"Dollis Hill" : 2, "Kilburn" : 2},
    "Kilburn" : {"Willesden Green" : 2, "West Hampstead" : 2},
    "West Hampstead" : {"Kilburn" : 2, "Finchley Road" : 1},
    "Finchley Road" : {"West Hampstead" : 1, "Swiss Cottage" : 2, "Wembley Park" : 7,"Baker Street": 5},
    "Swiss Cottage" : {"Finchley Road" : 2, "St. John's Wood" :2},
    "St. John's Wood" : {"Swiss Cottage" : 2, "Baker Street" : 3 },
    "Green Park" : {"Bond Street" : 2, "Westminster" :2, "Piccadilly Circus" : 2, "Hyde Park Corner" : 2, "Oxford Circus" : 2, "Victoria" : 2},
    "Waterloo" : {"Westminster" : 2, "Southwark" : 2, "Bank" : 5},
    "Southwark" : {"Waterloo" :2, "London Bridge" : 2},
    "London Bridge" : {"Southwark" :2, "Bermondsey" : 2 , "Bank" : 2, "Borough" : 2},
    "Bermondsey" : {"London Bridge" :2, "Canada Water" :2},
    "Canada Water" : {"Bermondsey" : 2, "Canary Wharf" : 3},
    "Canary Wharf" : {"Canada Water" : 3, "North Greenwich" :3},
    "North Greenwich" : {"Canary Wharf" : 3, "Canning Town" : 3},
    "Canning Town" : {"North Greenwich" :3, "West Ham" : 3},
    "Stratford" : {"West Ham" : 2},

    # Metropolitan
    "Amersham" : {"Chalfont & Latimer" : 4},
    "Chesham" : {"Chalfont & Latimer" : 4},
    "Chalfont & Latimer": {"Amersham" : 4, "Chesham" : 4, "Chorleywood" : 4},
    "Chorleywood" : {"Chalfont & Latimer" : 4, "Rickmansworth" : 4},
    "Rickmansworth" : {"Chorleywood"  :4, "Moor Park" : 4},
    "Moor Park" : {"Rickmansworth" : 4, "Croxley" : 4, "Northwood" :3, "Harrow-on-the-Hill" : 14},
    "Watford" : {"Croxley" : 4 },
    "Croxley" : {"Watford" : 4, "Moor Park" : 4},
    "Uxbridge" : {"Hillingdon" : 4},
    "Hillingdon" : {"Uxbridge" :4 , "Ickenham" : 2},
    "Ickenham" : {"Hillingdon" : 2 ,"Ruislip": 2},
    "Ruislip" : {"Ickenham" : 2, "Ruislip Manor" : 2},
    "Ruislip Manor" : {"Ruislip" : 2,"Eastcote" : 2},
    "Eastcote" : {"Ruislip Manor" :2 , "Rayners Lane" :2},
    "Rayners Lane" : {"Eastcote" :2 ,"West Harrow" : 3},
    "West Harrow" : {"Rayners Lane": 3,"Harrow-on-the-Hill" : 2},
    "Harrow-on-the-Hill" : {"West Harrow" : 2, "North Harrow" : 3, "Moor Park" : 14,"Northwick Park" : 3 , "Finchley Road" : 16, "Wembley Park" : 9},
    "North Harrow" : {"Harrow-on-the-Hill" : 3, "Pinner" : 2},
    "Pinner" : {"North Harrow" : 2, "Northwood Hills" :3},
    "Northwood Hills" : {"Pinner" :3 , "Northwood" : 3},
    "Northwood" : {"Northwood Hills" :3, "Moor Park" : 3},
    "Northwick Park" : {"Harrow-on-the-Hill" : 3, "Preston Road" : 3},
    "Preston Road" : {"Northwick Park" : 3,"Wembley Park" : 3},

    # Northern
    "High Barnet" :{"Totteridge & Whetstone" : 4},
    "Totteridge & Whetstone" : {"High Barnet" : 4, "Woodside Park" :2},
    "Woodside Park" : {"Totteridge & Whetstone" : 2, "West Finchley" : 2},
    "West Finchley" : {"Woodside Park" : 2, "Finchley Central"  :2},
    "Mill Hill East" : {"Finchley Central" : 4},
    "Finchley Central" : {"West Finchley" : 2, "Mill Hill East" : 4,"East Finchley" : 4},
    "East Finchley" : {"Finchley Central" : 4, "Highgate" : 3},
    "Highgate" : {"East Finchley" : 3, "Archway" : 3},
    "Archway" : {"Highgate" : 3 , "Tufnell Park" : 2},
    "Tufnell Park" : {"Archway" : 2, "Kentish Town" : 1},
    "Kentish Town" : {"Tufnell Park" : 1, "Camden Town" : 2},
    "Edgware" : {"Burnt Oak"  :4},
    "Burnt Oak" : {"Edgware" : 4,"Colindale" : 2},
    "Colindale" : {"Burnt Oak" : 2, "Hendon Central" : 3},
    "Hendon Central" : {"Colindale" : 3, "Brent Cross" : 2},
    "Brent Cross" : {"Hendon Central"  :2, "Golders Green" : 3},
    "Golders Green" : {"Brent Cross" : 3 , "Hampstead" : 4},
    "Hampstead" : {"Golders Green" : 4, "Belsize Park" : 3},
    "Belsize Park" : {"Hampstead"  :3, "Chalk Farm" : 2},
    "Chalk Farm" : {"Belsize Park" : 2, "Camden Town" : 1},
    "Camden Town" : {"Chalk Farm" : 1, "Mornington Crescent" : 2,"Kentish Town" : 2, "Euston" : 4},
    "Mornington Crescent" : {"Camden Town" : 2, "Euston" : 2},
    "Euston" : {"Mornington Crescent" : 2, "Warren Street" : 2,"Camden Town" : 4, "King's Cross St. Pancras" : 2},
    "Warren Street" : {"Euston" : 1, "Goodge Street" : 2, "Oxford Circus" : 2},
    "Goodge Street" : {"Warren Street" : 2 , "Tottenham" : 1},
    "Leicester Square" : {"Tottenham" : 2, "Charing Cross" : 1, "Covent Garden" : 1, "Piccadilly Circus" :1 },
    "Kennington" : {"Waterloo" : 3, "Elephant & Castle" : 2, "Oval" :3},
    "Angel" :{"King's Cross St. Pancras" : 3, "Old Street" : 3},
    "Old Street" : {"Angel" : 3, "Moorgate" : 2},
    "Borough" : {"London Bridge" : 2, "Elephant & Castle" : 2},
    "Oval" : {"Kennington" : 3, "Stockwell" :2},
    "Stockwell" : {"Oval" : 2, "Clapham North" :2 , "Vauxhall" : 3, "Brixton" : 2},
    "Clapham North" : {"Stockwell" : 2, "Clapham Common" :2},
    "Clapham Common" : {"Clapham North" :2,"Clapham South" :2},
    "Clapham South" : {"Clapham Common" : 2,"Balham" : 2},
    "Balham" : {"Clapham South" : 2, "Tooting Bec" : 2},
    "Tooting Bec" : {"Balham" : 2, "Tooting Broadway" : 2},
    "Tooting Broadway" : {"Tooting Bec" : 2, "Colliers Wood" : 2},
    "Colliers Wood" : {"Tooting Broadway" : 2, "South Wimbledon" : 2},
    "South Wimbledon" : {"Colliers Wood" : 2, "Morden" : 3},
    "Morden" : {"South Wimbledon" : 3},

    # Piccadilly
    "Cockfosters" : {"Oakwood" : 2},
    "Oakwood" : {"Cockfosters" : 2, "Southgate" : 3},
    "Southgate" : {"Oakwood" : 3, "Arnos Grove"  :4},
    "Arnos Grove" : {"Southgate" : 4 , "Bounds Green" : 2},
    "Bounds Green" : {"Arnos Grove" : 2, "Wood Green" : 3},
    "Wood Green" : {"Bounds Green" : 2, "Turnpike Lane" :2},
    "Turnpike Lane" : {"Wood Green" :2 ,"Manor House" : 4},
    "Manor House" : {"Turnpike Lane" : 4, "Finsbury Park" : 2},
    "Finsbury Park" : {"Manor House" : 2, "Arsenal" :1, "Seven Sisters" : 5, "Highbury & Islington" : 2},
    "Arsenal" : {"Finsbury Park" : 1, "Holloway Road" : 2},
    "Holloway Road" : {"Arsenal" : 2, "Caledonian Road" : 2},
    "Caledonian Road" : {"King's Cross St. Pancras" : 4},
    "Russell Square" : {"King's Cross St. Pancras" : 2, "Holborn" : 2},
    "Covent Garden" : {"Holborn" : 2, "Leicester Square" : 1},
    "Hyde Park Corner" : {"Green Park" : 2, "Knightsbridge" :2},
    "Knightsbridge" : {"Hyde Park Corner" : 2, "South Kensington" : 2},
    "Barons Court" : { "Earl's Court" : 3, "Osterley" :3},
    "Osterley" : {"Barons Court" : 3, "Hounslow East" : 2},
    "Hounslow East" : {"Osterley" : 2 , "Hounslow Central" : 1},
    "Hounslow Central" : {"Hounslow East" : 1, "Hounslow West" : 3},
    "Hounslow West" : {"Hounslow Central" : 3, "Hatton Cross" : 4},
    "Hatton Cross" : {"Hounslow West" : 4, "Heathrow Terminals 1, 2, 3" : 4, "Heathrow Terminal 4" : 3},
    "Heathrow Terminal 4" : {"Hatton Cross" : 3},
    "Heathrow Terminals 1, 2, 3" : {"Hatton Cross" : 4,"Heathrow Terminal 5" : 4},
    "Heathrow Terminal 5" : {"Heathrow Terminals 1, 2, 3" : 4},
    "North Ealing" : {"Ealing Common" : 2, "Park Royal" : 2},
    "Park Royal" : {"North Ealing" : 2, "Alperton" : 2},
    "Alperton" : {"Park Royal" : 2, "Sudbury Town" : 3},
    "Sudbury Town" : {"Alperton" : 3, "Sudbury Hill" : 2},
    "Sudbury Hill" : {"Sudbury Town" : 2 , "South Harrow" : 3},
    "South Harrow" : {"Sudbury Hill" : 3, "Rayners Lane" : 5},
    "Rayners Lane" : {"South Harrow" : 5, "Eastcote" : 2},
    "Eastcote" : {"Rayners Lane" : 2,  "Ruislip Manor" : 2},
    "Ruislip Manor" : {"Eastcote" : 2 ,"Ruislip" : 2},
    "Ruislip" : {"Ruislip Manor" : 2, "Ickenham" : 4},
    "Ickenham" : {"Ruislip" : 4, "Hillingdon" : 2},
    "Hillingdon" : {"Ickenham" : 2, "Uxbridge" : 4},
    "Uxbridge" : {"Hillingdon" : 4},

    # Victoria
    "Walthamstow Central" : {"Blackhorse Road" :3},
    "Blackhorse Road" : {"Walthamstow Central" : 3, "Tottenham Hale" : 3},
    "Tottenham Hale" : {"Blackhorse Road" : 3, "Seven Sisters" : 2},
    "Seven Sisters" : {"Tottenham Hale" : 2, "Finsbury Park" : 5},
    "Highbury & Islington" : {"Finsbury Park" : 2, "King's Cross St. Pancras" : 3},
    "Pimlico" : {"Victoria" : 2, "Vauxhall" : 2},
    "Vauxhall" : {"Pimlico" : 2, "Stockwell" : 3},
    "Brixton" : {"Stockwell" : 2}

    # Waterloo & City

}

def dijkstra(graph,start,goal):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = 999999
    track_path = []

    for node in unseenNodes :
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]

        except KeyError :
            print("Path is not reachable")
            break

    track_path.insert(0,start)

    if shortest_distance[goal] != infinity:
        print("Shortest distance is " + str(shortest_distance[goal]))
        print("Optimal path is " + str(track_path))

dijkstra(graph, "Kenton", "Brixton")