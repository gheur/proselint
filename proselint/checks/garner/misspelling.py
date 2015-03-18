# -*- coding: utf-8 -*-
"""MAU102: Misspellings.

---
layout:     post
error_code: MAU102
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      misspellings
date:       2014-06-10 12:31:19
categories: writing
---

Points out misspellings.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "Misspelling. '{}' is the preferred form."

    misspellings = [
        ["academically",      ["academicly"]],
        ["accidentally",      ["accidently"]],
        ["accommodable",      ["accomodatable"]],
        ["anilingus",         ["analingus"]],
        ["aren't i",          ["amn't i"]],
        ["aren't i",          ["an't i"]],
        ["chargeable",        ["chargable"]],
        ["chiffonier",        ["chiffonnier"]],
        ["chintzy",           ["chinchy"]],
        ["chipotle",          ["chipolte"]],
        ["chlorophyll",       ["chlorophyl"]],
        ["chocolaty",         ["chocolatey"]],
        ["chronicle",         ["chronical"]],
        ["chronicles",        ["chronicals"]],
        ["coleslaw",          ["coldslaw"]],
        ["choosy",            ["choosey"]],
        ["cummerbund",        ["kummerbund"]],
        ["financeable",       ["financable"]],
        ["fluorescent",       ["flourescent"]],
        ["fluoridation",      ["flouridation"]],
        ["fluoride",          ["flouride"]],
        ["foreclose",         ["forclose"]],
        ["forswear",          ["foreswear"]],
        ["free rein",         ["free reign"]],
        ["gist",              ["jist"]],
        ["glamour",           ["glamor"]],
        ["granddad",          ["grandad"]],
        ["grandpa",           ["granpa"]],
        ["highfalutin",       ["highfaluting", "highfalutin'", "hifalutin"]],
        ["Hippocratic",       ["hypocratic"]],
        ["hirable",           ["hireable"]],
        ["holistic",          ["wholistic"]],
        ["ideology",          ["idealogy"]],
        ["idiosyncrasy",      ["ideosyncracy"]],
        ["improvise",         ["improvize"]],
        ["incurrence",        ["incurment"]],
        ["inevitability",     ["inevitableness"]],
        ["innovate",          ["inovate"]],
        ["inoculation",       ["innoculation", "inocculation"]],
        ["integral",          ["intergral"]],
        ["inundate",          ["innundate"]],
        ["inundated",         ["innundated"]],
        ["inundates",         ["innundates"]],
        ["inundating",        ["innundating"]],
        ["iridescent",        ["irridescent"]],
        ["jujitsu",           ["jiujutsu"]],
        ["kaleidoscope",      ["kaleidascope"]],
        ["knickknack",        ["knicknack"]],
        ["lassos",            ["lassoes"]],
        ["lessee",            ["leasee"]],
        ["lessor",            ["leasor"]],
        ["liquefy",           ["liquify"]],
        ["loathsome",         ["loathesome"]],
        ["to make do",        ["to make due"]],
        ["mademoiselle",      ["madamoiselle"]],
        ["minuscule",         ["miniscule"]],
        ["mischievous",       ["mischievious"]],
        ["newsstand",         ["newstand"]],
        ["occurred",          ["occured"]],
        ["plantar fasciitis", ["planter fasciitis", "plantar fascitis"]],
        ["pledgeable",        ["pledgable", "pledgeble"]],
        ["portentous",        ["portentuous", "portentious"]],
        ["praying mantis",    ["preying mantis"]],
        ["preestablished",    ["prestablished"]],
        ["preexisting",       ["prexisting"]],
        ["presumptuous",      ["presumptious"]],
        ["reckless",            ["wreckless"]],
        ["remuneration",      ["renumeration"]],
        ["restaurateur",      ["restauranteur"]],
        ["retractable",       ["retractible"]],
        ["reverie",           ["revery"]],
        ["spicy",             ["spicey"]],
        ["stupefy",           ["stupify"]],
        ["subtly",            ["subtley"]],
        ["till",              ["\'till?"]],
        ["tinderbox",         ["tenderbox"]],
        ["timpani",           ["tympani"]],
        ["a timpani",         ["a timpano"]],
    ]

    return preferred_forms_check(blob, misspellings, err, msg)