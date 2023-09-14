package main

import (
	"archive/zip"
	"io"
	"os"
	"path/filepath"
)

type FileExtractor struct {
	ZipPath string
	DestDir string
}

func (fe *FileExtractor) extract() error {
	r, err := zip.OpenReader(fe.ZipPath)
	if err != nil {
		return err
	}
	defer r.Close()

	for _, f := range r.File {
		rc, err := f.Open()
		if err != nil {
			return err
		}
		defer rc.Close()

		path := filepath.Join(fe.DestDir, f.Name)
		if f.FileInfo().IsDir() {
			os.MkdirAll(path, f.Mode())
		} else {
			file, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, f.Mode())
			if err != nil {
				return err
			}
			defer file.Close()

			_, err = io.Copy(file, rc)
			if err != nil {
				return err
			}
		}
	}

	return nil
}