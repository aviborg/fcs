
% ==== Simulink Export Automation Script ====
model = 'YourModelName'; % <-- Replace with your model name
load_system(model);

% Create export directory if not existing
outputDir = fullfile(pwd, 'exports');
if ~exist(outputDir, 'dir')
    mkdir(outputDir);
end

% 1. Export Model Structure
blocks = find_system(model, 'Type', 'Block');
fid = fopen(fullfile(outputDir, 'model_structure.txt'), 'w');
for i = 1:length(blocks)
    fprintf(fid, '%s\n', blocks{i});
end
fclose(fid);

% 2. Export Requirements Trace
reqSet = slreq.find('Type','ReqSet');
if ~isempty(reqSet)
    slreq.export(reqSet, fullfile(outputDir, 'req_trace.xml'));
end

% 3. Export Requirements as CSV
links = slreq.find('Type','Link');
fid = fopen(fullfile(outputDir, 'req_trace.csv'), 'w');
fprintf(fid, 'ID,Source,Destination\n');
for i = 1:length(links)
    src = links(i).Source;
    dest = links(i).Destination;
    fprintf(fid, '%s,%s,%s\n', links(i).ID, src.Artifact, dest.Artifact);
end
fclose(fid);

% 4. Export Test Results (if using Simulink Test)
try
    sltest.testmanager.report(fullfile(outputDir, 'test_results.html'), ...
        'IncludeTestResults', true, ...
        'IncludeTestRequirements', true, ...
        'IncludeCoverage', true);
catch ME
    disp('Test Manager report export failed:');
    disp(ME.message);
end

% 5. Export Coverage Results
try
    cvdo = cvsim(model); % Simulate for coverage
    cvhtml(fullfile(outputDir, 'coverage_report'), cvdo);
    cvsave(fullfile(outputDir, 'coverage_data'), cvdo);
catch ME
    disp('Coverage export failed:');
    disp(ME.message);
end

disp('Export complete.');
