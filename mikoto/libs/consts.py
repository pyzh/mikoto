IGNORE_FILE_EXTS = (
    '.tar', '.zip', '.rar', '.gz', '.bz', '.bz2',
    '.bmp', '.jpeg', '.jpg', '.png', '.gif', '.svg', '.ico',
    '.mp3', '.svn-base', '.swf', '.ttf', '.jar', '.fla', '.flash', '.pdf',
    '.wmv', '.asf', '.asx', '.rm', '.rmvb', '.mpg', '.mpeg', '.mpe', '.pcap',
    '.3gp', '.mov', '.mp4', '.m4v', '.avi', '.dat', '.mkv', '.flv', '.vob',
    '.dmg',
)

IS_GENERATED = ('.xib', '.nib', '.storyboard', '.pbxproj', '.xcworkspacedata',
                '.xcuserstate')

NOT_GENERATED = ('.py', '.html', '.mako', '.css', '.txt', '.rst', '.md',
                 '.mkd', '.markdown', '.sh', '.sql', '.ini', '.gitignore',
                 '.tmpl', '.cfg', '.hgignore', '.gitmodules', '.AUTHORS',
                 ".scss", ".coffee", '.conf', '.applescript', '.thrift',
                 '.log', '.json', '.gradle', '.ebuild', '.vimrc', '.bashrc',
                 '.zshrc', '.tmux.conf', '.aliases', '.bash_profile',
                 '.bash_prompt', '.exports', '.gitconfig', '.inputrc',
                 '.functions')
MINIFIED = ('.min.js', '.min.css')
PICS = ('.jpeg', '.jpg', '.png', '.gif')

LANGUAGES = {
            'abap'        : 'ABAP'                  ,
            'ac'          : 'm4'                    ,
            'ada'         : 'Ada'                   ,
            'adb'         : 'Ada'                   ,
            'ads'         : 'Ada'                   ,
            'adso'        : 'ADSO/IDSM'             ,
            'am'          : 'make'                  ,
            'ample'       : 'AMPLE'                 ,
            'as'          : 'ActionScript'          ,
            'dofile'      : 'AMPLE'                 ,
            'startup'     : 'AMPLE'                 ,
            'asa'         : 'ASP'                   ,
            'asax'        : 'ASP.Net'               ,
            'ascx'        : 'ASP.Net'               ,
            'asm'         : 'Assembly'              ,
            'asmx'        : 'ASP.Net'               ,
            'asp'         : 'ASP'                   ,
            'aspx'        : 'ASP.Net'               ,
            'master'      : 'ASP.Net'               ,
            'sitemap'     : 'ASP.Net'               ,
            'awk'         : 'awk'                   ,
            'bash'        : 'Bourne Again Shell'    ,
            'bas'         : 'Visual Basic'          ,
            'bat'         : 'DOS Batch'             ,
            'BAT'         : 'DOS Batch'             ,
            'cbl'         : 'COBOL'                 ,
            'CBL'         : 'COBOL'                 ,
            'c'           : 'C'                     ,
            'C'           : 'C++'                   ,
            'cc'          : 'C++'                   ,
            'ccs'         : 'CCS'                   ,
            'cfm'         : 'ColdFusion'            ,
            'cl'          : 'Lisp'                  ,
            'cls'         : 'Visual Basic'          ,
            'cob'         : 'COBOL'                 ,
            'COB'         : 'COBOL'                 ,
            'coffee'      : 'CoffeeScript'          ,
            'config'      : 'ASP.Net'               ,
            'cpp'         : 'C++'                   ,
            'cs'          : 'C#'                    ,
            'csh'         : 'C Shell'               ,
            'css'         : "CSS"                   ,
            'cxx'         : 'C++'                   ,
            'd'           : 'D'                     ,
            'da'          : 'DAL'                   ,
            'dart'        : 'Dart'                  ,
            'def'         : 'Teamcenter def'        ,
            'dmap'        : 'NASTRAN DMAP'          ,
            'dpr'         : 'Pascal'                ,
            'dtd'         : 'DTD'                   ,
            'ec'          : 'C'                     ,
            'el'          : 'Lisp'                  ,
            'erl'         : 'Erlang'                ,
            'exp'         : 'Expect'                ,
            'f77'         : 'Fortran 77'            ,
            'F77'         : 'Fortran 77'            ,
            'f90'         : 'Fortran 90'            ,
            'F90'         : 'Fortran 90'            ,
            'f95'         : 'Fortran 95'            ,
            'F95'         : 'Fortran 95'            ,
            'f'           : 'Fortran 77'            ,
            'F'           : 'Fortran 77'            ,
            'fmt'         : 'Oracle Forms'          ,
            'focexec'     : 'Focus'                 ,
            'frm'         : 'Visual Basic'          ,
            'go'          : 'Go'                    ,
            'groovy'      : 'Groovy'                ,
            'h'           : 'C/C++ Header'          ,
            'H'           : 'C/C++ Header'          ,
            'hh'          : 'C/C++ Header'          ,
            'hpp'         : 'C/C++ Header'          ,
            'hrl'         : 'Erlang'                ,
            'hs'          : 'Haskell'               ,
            'htm'         : 'HTML'                  ,
            'html'        : 'HTML'                  ,
            'i3'          : 'Modula3'               ,
            'idl'         : 'IDL'                   ,
            'pro'         : 'IDL'                   ,
            'ig'          : 'Modula3'               ,
            'il'          : 'SKILL'                 ,
            'ils'         : 'SKILL++'               ,
            'inc'         : 'PHP/Pascal'            , # might be PHP or Pascal
            'itk'         : 'Tcl/Tk'                ,
            'java'        : 'Java'                  ,
            'jcl'         : 'JCL'                   , # IBM Job Control Lang.
            'jl'          : 'Lisp'                  ,
            'js'          : 'Javascript'            ,
            'jsp'         : 'JSP'                   , # Java server pages
            'ksc'         : 'Kermit'                ,
            'ksh'         : 'Korn Shell'            ,
            'lhs'         : 'Haskell'               ,
            'l'           : 'lex'                   ,
            'lsp'         : 'Lisp'                  ,
            'lisp'        : 'Lisp'                  ,
            'lua'         : 'Lua'                   ,
            'm3'          : 'Modula3'               ,
            'm4'          : 'm4'                    ,
            'met'         : 'Teamcenter met'        ,
            'mg'          : 'Modula3'               ,
#           'mli'         : 'ML'                    , # ML not implemented
#           'ml'          : 'ML'                    ,
            'ml'          : 'Ocaml'                 ,
            'm'           : 'MATLAB/Objective C/MUMPS' ,
            'mm'          : 'Objective C++'         ,
            'wdproj'      : 'MSBuild scripts'       ,
            'csproj'      : 'MSBuild scripts'       ,
            'mps'         : 'MUMPS'                 ,
            'mth'         : 'Teamcenter mth'        ,
            'oscript'     : 'LiveLink OScript'      ,
            'pad'         : 'Ada'                   , # Oracle Ada preprocessor
            'pas'         : 'Pascal'                ,
            'pcc'         : 'C++'                   , # Oracle C++ preprocessor
            'perl'        : 'Perl'                  ,
            'pfo'         : 'Fortran 77'            ,
            'pgc'         : 'C'                     , # Postgres embedded C/C++
            'php3'        : 'PHP'                   ,
            'php4'        : 'PHP'                   ,
            'php5'        : 'PHP'                   ,
            'php'         : 'PHP'                   ,
            'plh'         : 'Perl'                  ,
            'pl'          : 'Perl'                  ,
            'PL'          : 'Perl'                  ,
            'plx'         : 'Perl'                  ,
            'pm'          : 'Perl'                  ,
            'p'           : 'Pascal'                ,
            'pp'          : 'Pascal'                ,
            'psql'        : 'SQL'                   ,
            'py'          : 'Python'                ,
            'pyx'         : 'Cython'                ,
            'rb'          : 'Ruby'                  ,
            'R'           : 'R'                     ,
         #  'resx'        : 'ASP.Net'               ,
            'rex'         : 'Oracle Reports'        ,
            'rexx'        : 'Rexx'                  ,
            'rhtml'       : 'Ruby HTML'             ,
            's'           : 'Assembly'              ,
            'S'           : 'Assembly'              ,
            'scala'       : 'Scala'                 ,
            'scss'        : 'SCSS'                  ,
            'sbl'         : 'Softbridge Basic'      ,
            'SBL'         : 'Softbridge Basic'      ,
            'sc'          : 'Lisp'                  ,
            'scm'         : 'Lisp'                  ,
            'sed'         : 'sed'                   ,
            'ses'         : 'Patran Command Language'   ,
            'pcl'         : 'Patran Command Language'   ,
            'sh'          : 'Bourne Shell'          ,
            'smarty'      : 'Smarty'                ,
            'sql'         : 'SQL'                   ,
            'stylus'      : 'Stylus'                ,
            'SQL'         : 'SQL'                   ,
            'sproc.sql'   : 'SQL Stored Procedure'  ,
            'spoc.sql'    : 'SQL Stored Procedure'  ,
            'spc.sql'     : 'SQL Stored Procedure'  ,
            'udf.sql'     : 'SQL Stored Procedure'  ,
            'data.sql'    : 'SQL Data'              ,
            'tcl'         : 'Tcl/Tk'                ,
            'tcsh'        : 'C Shell'               ,
            'tk'          : 'Tcl/Tk'                ,
            'tpl'         : 'Smarty'                ,
            'vhd'         : 'VHDL'                  ,
            'VHD'         : 'VHDL'                  ,
            'vhdl'        : 'VHDL'                  ,
            'VHDL'        : 'VHDL'                  ,
            'vba'         : 'Visual Basic'          ,
            'VBA'         : 'Visual Basic'          ,
         #  'vbp'         : 'Visual Basic'          , # .vbp - autogenerated
            'vb'          : 'Visual Basic'          ,
            'VB'          : 'Visual Basic'          ,
         #  'vbw'         : 'Visual Basic'          , # .vbw - autogenerated
            'vbs'         : 'Visual Basic'          ,
            'VBS'         : 'Visual Basic'          ,
            'webinfo'     : 'ASP.Net'               ,
            'xml'         : 'XML'                   ,
            'XML'         : 'XML'                   ,
            'mxml'        : 'MXML'                  ,
            'build'       : 'NAnt scripts'          ,
            'vim'         : 'vim script'            ,
            'xaml'        : 'XAML'                  ,
            'xsd'         : 'XSD'                   ,
            'XSD'         : 'XSD'                   ,
            'xslt'        : 'XSLT'                  ,
            'XSLT'        : 'XSLT'                  ,
            'xsl'         : 'XSLT'                  ,
            'XSL'         : 'XSLT'                  ,
            'y'           : 'yacc'                  ,
            'yaml'        : 'YAML'                  ,
            'yml'         : 'YAML'                  ,
            }

LANGUAGES_WITHOUT_EXT = {
    'CMakeLists.txt': 'CMake',
    'Cakefile': 'CoffeeScript',
    'gnumakefile': 'make',
    'Gnumakefile': 'make',
    'makefile': 'make',
    'Makefile': 'make',
    'Rakefile': 'Ruby',
}

SOURCE_FILE = (tuple(['.' + ext for ext in LANGUAGES.keys()]) +
               tuple(LANGUAGES_WITHOUT_EXT.keys()))
