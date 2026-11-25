DNA=set("ACGT")


def process(data):
    reference=data.get("reference") if isinstance(data,dict) else None
    variants=data.get("variants") if isinstance(data,dict) else None
    if not isinstance(reference,str) or not 1<=len(reference)<=1000000 or set(reference)-DNA: raise ValueError("reference must be uppercase ACGT")
    if not isinstance(variants,list) or not 1<=len(variants)<=10000: raise ValueError("variants must contain 1..10000 items")
    ids=set(); results=[]; canonical={}
    for row in variants:
        vid=row.get("id") if isinstance(row,dict) else None; pos=row.get("pos") if isinstance(row,dict) else None
        ref=row.get("ref") if isinstance(row,dict) else None; alt=row.get("alt") if isinstance(row,dict) else None
        if not isinstance(vid,str) or not vid or vid in ids: raise ValueError("variant ids must be unique")
        if isinstance(pos,bool) or not isinstance(pos,int) or pos<1: raise ValueError("pos must be 1-based integer")
        if not isinstance(ref,str) or not isinstance(alt,str) or not ref or not alt or set(ref+alt)-DNA: raise ValueError("ref and alt must be nonempty ACGT")
        if pos-1+len(ref)>len(reference) or reference[pos-1:pos-1+len(ref)]!=ref: raise ValueError("reference allele mismatch")
        ids.add(vid)
        while len(ref)>1 and len(alt)>1 and ref[-1]==alt[-1]: ref=ref[:-1]; alt=alt[:-1]
        while len(ref)>1 and len(alt)>1 and ref[0]==alt[0]: ref=ref[1:]; alt=alt[1:]; pos+=1
        while len(ref)!=len(alt) and pos>1:
            preceding=reference[pos-2]
            if not (preceding == ref[-1] == alt[-1]):
                break
            ref=preceding+ref[:-1]; alt=preceding+alt[:-1]; pos-=1
        key=(pos,ref,alt)
        canonical.setdefault(key,[]).append(vid)
        results.append({"id":vid,"pos":pos,"ref":ref,"alt":alt,"canonical_key":f"{pos}:{ref}>{alt}"})
    groups=[{"canonical_key":f"{pos}:{ref}>{alt}","variant_ids":sorted(group)} for (pos,ref,alt),group in sorted(canonical.items())]
    return {"variants":sorted(results,key=lambda x:x["id"]),"equivalence_groups":groups}
