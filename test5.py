import re
info=(re.findall(".* Diag \((.*)\)\n\
.* build .* \(.*\)\. Revision .*\.\n\
Built at .*","pro Diag (branch.000)\n\
engin build version (diags_version). Revision revision.\n\
Built at build_date_time"))
print(info)